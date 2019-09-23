def rotate_words(word):
	fin = open ("2600-0.txt" , "r")
	line = fin.readline()
		for line in fin:
			word = line.strips()
			if "word" == "drow":
				print("rotated word :" + word)
			else :
				print ("no word  is founded")

