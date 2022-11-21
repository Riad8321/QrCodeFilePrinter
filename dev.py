import cv2
import os
import time
import urllib.request



cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS,12)

detector = cv2.QRCodeDetector()

def download_file(download_url, filename):
            response = urllib.request.urlopen(download_url)    
            file = open(filename + ".pdf", 'wb')
            file.write(response.read())
            file.close()

liste_urls = [""]

while True:
    check, img = cap.read()
    data2, bbox, _ = detector.detectAndDecode(img)

   # if(bbox is not None):
      #  for i in range (len(bbox)):
      #      cv2.line(img, tuple(bbox[i][0]), tuple(bbox[(i+1) % len(bbox)][0]), color = (0, 0, 255), thickness = )
       #     cv2.putText(img, data, (int(bbox[0][0][0]), int(bbox[0][0][1]) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255, 0, 0), 2)   
    if data2:
        data = data2
        if data not in liste_urls:
            print(data)
            print(liste_urls)
            pdf_path = str(data)
            download_file(pdf_path, "Test2")
            liste_urls.extend([data])
            os.system("lpr -P Canon_MG5700_series test2.pdf")
            os.remove("file_Downloaded.pdf")
    
    cv2.imshow("image", img)

    if(cv2.waitKey(1) == ord("q")):
        break

cap.release()
cv2.destroyAllWindows()
