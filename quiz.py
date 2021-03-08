class Question:
	def __init__(self, quest, answer):
		self.quest = quest
		self.answer = answer

quest_promt = [
	"Dalam menyusun suatu program,langkah pertama yang harus di lakkukan adalah :\n\t(a) membuat program\n\t(b) membuat algoritma\n\t(c) membeli komputer\n\t(d) proses\n\t(e) mempelajari program\nJawab : ",
	"\nSebuah prosedur langkah demi langkah yang pasti untuk menyelesaikan sebuah masalah di sebut :\n\t(a) proses\n\t(b) program\n\t(c) algoritma\n\t(d) step\n\t(e) diagram\nJawab : ",
	"\nPseudocode yang di gunakan pada penulisan algoritma berupa :\n\t(a) bahasa inggris\n\t(b) bahasa puitis\n\t(c) bahasa pemrograman\n\t(d) sembarang bahasa asal terstruktur\n\t(e) bahasa mesin\nJawab : ",
	"\nPada pembuatan program komputer, algoritma dibuat :\n\t(a) sebelum pembuatan program\n\t(b) pada saat program dibuat\n\t(c) sesudah pembuatan program\n\t(d) pada saat verivikasi program\n\t(e) pada saat dijalankan\nJawab : ",
	"\nDiberikan algoritma : Apabila warna merah maka jadi hijau. Apabila warna hijau maka jadi putih, selain warna merah dan hijau maka jadi ungu. Jika kondisi input warna adalah hitam, maka warna jadi :\n\t(a) merah\n\t(b) ungu\n\t(c) hijau\n\t(d) putih\n\t(e) abu-abu\nJawab : "
]

name = input("Masukkan nama: ").title()
questions = [
	Question(quest_promt[0], 'b'),
	Question(quest_promt[1], 'c'),
	Question(quest_promt[2], 'c'),
	Question(quest_promt[3], 'a'),
	Question(quest_promt[4], 'b')
]

def quiz_run(questions):
	score = 0
	for question in questions:
		user_answer = input(question.quest)
		if user_answer == question.answer:
			score += 1
	print(f'\n{name}, skor kamu {score} dari {len(questions)}')

quiz_run(questions)
