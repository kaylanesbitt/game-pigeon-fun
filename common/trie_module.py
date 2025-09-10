import pickle
import requests
import os

class TrieNode: 
    def __init__(self): 
        self.children = {}
        self.is_word = False

class Trie: 
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word): 
        node = self.root
        for ch in word: 
            if ch not in node.children: 
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_word = True
    
    def search(self, word): 
        node = self.root
        for ch in word: 
            if ch not in node.children: 
                return False
            node = node.children[ch]
        return node.is_word
    
    def is_prefix(self, prefix): 
        node = self.root
        for ch in prefix: 
            if ch not in node.children: 
                return False
            node = node.children[ch]
        return True
    
    def pretty_print(self, node=None, prefix=""):
        if node is None:
            node = self.root

        for ch, child in node.children.items():
            if child.is_word:
                print(f"{prefix}{ch}*")  # * marks end of word
            else:
                print(f"{prefix}{ch}")
            self.pretty_print(child, prefix + "  ")  # indent children
