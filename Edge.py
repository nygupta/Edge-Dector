import cv2 
from matplotlib import pyplot as plt
def image(url):
	img = cv2.imread(url, 0)
	canny = cv2.Canny(img, 100, 200)
	titles = ['grayscale', 'edge']
	images = [img, canny]
	for i in range(2):
		plt.subplot(1, 2, i + 1), plt.imshow(images[i], 'gray')
		plt.title(titles[i])
		plt.xticks([]), plt.yticks([])
	plt.show()
def camcapture():
	cap = cv2.VideoCapture(0)
	while(1):
		ret, frame = cap.read()
		cv2.imshow('Original',frame)
		edges = cv2.Canny(frame,100,200)
		cv2.imshow('Edges',edges)
		if cv2.waitKey(1) & 0xFF ==ord('x'):
			break
	cap.release()
	cv2.destroyAllWindows() 

def main():
	print("1: if you have the image")
	print("2: if you want to start the camera")
	val = int(input())
	if val == 1:
		url = input("url of the image:")
		image(url)
	elif val == 2:
		camcapture()

main()