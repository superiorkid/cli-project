# install library speedtest-cli
import speedtest

speed  = speedtest.Speedtest()

def main():
	while True:

		choice = int(input("""
				Check your internet connection speed.\n
					1) download speed\n
					2) upload speed\n
					3) exit\n
				Choice(1/2/3): """))

		if choice == 1:
			print('Counting...')
			print('Download speed: {:.2f} Mb/s'.format(speed.download()/1024/1024))
		elif choice == 2:
			print('Counting...')
			print('Upload speed: {:.2f} Mb/s'.format(speed.upload()/1024/1024))
		elif choice == 3:
			print('Exiting the program')
			quit()
		else:
			print('please choose the correct options')

if __name__ == '__main__':
	main()
