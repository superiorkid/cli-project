"""
 tujuannya untuk membuat permainan berbasis command-line dimana user diberi kesempatan antara batu, gunting, kertas dan jika pengguna menang, skor akan ditampilkan kepada user
"""

import random

choices = ['gunting', 'batu', 'kertas']
comp = random.choice(choices)
player = False
comp_score = 0
player_score = 0
print('Permainan Gunting batu kertas.\ntekan \'E\' untuk keluar')
while True:
	player = input('Gunting/Batu/kertas? ').lower()
	if player == comp:
		print('Imbang!')
	elif player == 'batu':
		if comp == 'kertas':
			print(f'you lose!! {comp} membungkus {player}')
			comp_score += 1
		else:
			print(f'you win {player} smashes {comp}')
			player_score += 1
	elif player == 'kertas':
		if comp == 'gunting':
			print(f'you lose {comp} cut {player}')
			comp_score += 1
		else:
			print(f'you win	{player} covers {comp}')
			player_score += 1
	elif player == 'gunting':
		if comp == 'batu':
			print(f'you lose {comp} smashes {player}')
			comp_score += 1
		else:
			print(f'you win {player} cut {comp}')
			player_score += 1
	elif player == 'e':
		print('Final Score')
		print(f'computer score: {comp_score}')
		print(f'player score: {player_score}')
		break
	else:
		print('inputan salah')
	
	comp = random.choice(choices)




