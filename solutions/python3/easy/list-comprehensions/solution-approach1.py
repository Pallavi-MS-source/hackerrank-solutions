# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true
# Problem     List Comprehensions
# Difficulty  Easy
# Subdomain   Basic Data Types
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-30, 11:50 p.m.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    ans = [[i,j,k]
            for i in range(0,x + 1)
            for j in range(0,y + 1) 
            for k in range(0,z + 1) 
            if i + j + k != n ]
print(ans)
    
    
