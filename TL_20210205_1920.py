import time, cv2
current_time = time.time()
endtime = current_time + 12*60*60
cap = cv2.VideoCapture(0)

while current_time < endtime:
    img = cap.read()[1]
	cv2.imwrite('img_{}.png'.format(int(time.time())), img)
    time.sleep(30)

