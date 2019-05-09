#!/usr/bin/python

import sys

def rock_paper_scissors(n):
    plays = ['rock', 'paper', 'scissors']
    results = []    

    def rps_helper(n, result):
        if len(result) == n:
            return results.append(result)
        for play in plays:
            rps_helper(n, result + [play])

    rps_helper(n, [])
    return results

print(rock_paper_scissors(2))
        
if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')