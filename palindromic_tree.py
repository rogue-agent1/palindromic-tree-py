#!/usr/bin/env python3
"""Palindromic tree (Eertree) — all distinct palindromic substrings in O(n)."""

class PalNode:
    __slots__ = ("len","link","trans")
    def __init__(self, length, link=0): self.len=length; self.link=link; self.trans={}

class Eertree:
    def __init__(self):
        self.nodes = [PalNode(-1, 0), PalNode(0, 0)]  # root-1, root0
        self.s = [-1]; self.last = 1  # root0 = empty palindrome
    def _get_link(self, v):
        while self.s[-self.nodes[v].len-2] != self.s[-1]:
            v = self.nodes[v].link
        return v
    def add(self, c):
        self.s.append(c)
        cur = self._get_link(self.last)
        if c not in self.nodes[cur].trans:
            new = PalNode(self.nodes[cur].len + 2)
            q = self._get_link(self.nodes[cur].link)
            new.link = self.nodes[q].trans.get(c, 1)
            self.nodes[cur].trans[c] = len(self.nodes)
            self.nodes.append(new)
        self.last = self.nodes[cur].trans[c]
    def count(self): return len(self.nodes) - 2  # exclude two roots

def build(s):
    t = Eertree()
    for c in s: t.add(c)
    return t

def main():
    t = build("eertree")
    print(f"Distinct palindromic substrings: {t.count()}")

if __name__ == "__main__": main()
