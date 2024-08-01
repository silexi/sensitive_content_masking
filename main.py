# Author: Bartu KILIÇ
# Contact: kilicbartu@gmail.com
# GitHub: https://github.com/silexi
# Website: https://bartukilic.com

import os
import re
import shutil
from collections import defaultdict


REGEX_FILE = 'config/regex_patterns.txt'
KEYWORD_FILE = 'config/keywords.txt'


ALLOWED_FILE_EXTENSIONS = ['.txt', '.py', '.md', '.json', '.csv']

def load_patterns(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        patterns = [line.strip() for line in file.readlines()]
    return patterns

def mask_partial(match):
    match_str = match.group()
    if len(match_str) <= 2:
        return match_str  
    return match_str[0] + '*' * (len(match_str) - 2) + match_str[-1]

def mask_content(content, regex_patterns=None, keywords=None, stats=None):
    if regex_patterns:
        for pattern in regex_patterns:
            matches = re.findall(pattern, content)
            if matches:
                stats['regex'][pattern] += len(matches)
                content = re.sub(pattern, mask_partial, content)
    if keywords:
        for keyword in keywords:
            count = content.count(keyword)
            if count > 0:
                stats['keywords'][keyword] += count
                content = re.sub(re.escape(keyword), mask_partial, content)
    return content

def mask_file(file_path, regex_patterns=None, keywords=None, stats=None):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        masked_content = mask_content(content, regex_patterns, keywords, stats)
        
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(masked_content)
        
        print(f"Masked content in file: {file_path}")
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")

def mask_files_in_directory(directory_path, regex_patterns=None, keywords=None, stats=None):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.splitext(file_path)[1] in ALLOWED_FILE_EXTENSIONS:
                mask_file(file_path, regex_patterns, keywords, stats)

def print_stats(stats):
    print("\nMasking Statistics:")
    if stats['regex']:
        print("\nRegex Patterns:")
        for pattern, count in stats['regex'].items():
            print(f"{pattern}: {count} matches")
    if stats['keywords']:
        print("\nKeywords:")
        for keyword, count in stats['keywords'].items():
            print(f"{keyword}: {count} matches")

def main():
    choice = input("Dosya mı yoksa dizindeki tüm dosyalar için mi işlem yapmak istiyorsunuz? (dosya/dizin): ").strip().lower()
    stats = {'regex': defaultdict(int), 'keywords': defaultdict(int)}
    
    if choice == 'dosya':
        file_path = input("Lütfen dosya yolunu giriniz: ").strip()
        if os.path.isfile(file_path) and os.path.splitext(file_path)[1] in ALLOWED_FILE_EXTENSIONS:
            regex_patterns = []
            keywords = []
            print("İşlem seçin: [1- Regex, 2- Kelime, 3- Hepsi]")
            operation = input().strip()
            if operation in ['1', '3']:
                regex_patterns = load_patterns(REGEX_FILE)
            if operation in ['2', '3']:
                keywords = load_patterns(KEYWORD_FILE)
            mask_file(file_path, regex_patterns, keywords, stats)
        else:
            print("Geçersiz dosya yolu veya dosya formatı.")
    
    elif choice == 'dizin':
        directory_path = input("Lütfen dizin yolunu giriniz: ").strip()
        if os.path.isdir(directory_path):
            target_directory = f"{directory_path}_m"
            shutil.copytree(directory_path, target_directory)
            regex_patterns = []
            keywords = []
            print("İşlem seçin: [1- Regex, 2- Kelime, 3- Hepsi]")
            operation = input().strip()
            if operation in ['1', '3']:
                regex_patterns = load_patterns(REGEX_FILE)
            if operation in ['2', '3']:
                keywords = load_patterns(KEYWORD_FILE)
            mask_files_in_directory(target_directory, regex_patterns, keywords, stats)
        else:
            print("Geçersiz dizin yolu.")
    else:
        print("Geçersiz seçim.")
    
    print_stats(stats)

if __name__ == "__main__":
    main()
