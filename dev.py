import cv2
import os
import time
import urllib.request


# lancer la fenêtre de cpature vidéo
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS,12)

# detecter le qr code avec la webcam
detector = cv2.QRCodeDetector()

# fonction pour télécharger un fichier pdf
def download_file(download_url, filename):
            response = urllib.request.urlopen(download_url)    
            file = open(filename + ".pdf", 'wb')
            file.write(response.read())
            file.close()

# la liste des urls scannés sont stocké dans cette liste  
liste_urls = [""]

while True:
    check, img = cap.read()
    data2, bbox, _ = detector.detectAndDecode(img)
    if data2:
        data = data2
        # vérifie si l'url scanné n'est pas dans la liste
        if data not in liste_urls:
            print(data)
            print(liste_urls)
            pdf_path = str(data)
            download_file(pdf_path, "Test2")
            liste_urls.extend([data])
            os.system("lpr -P Canon_MG5700_series file_Downloaded.pdf")
            os.remove("file_Downloaded.pdf")
    
    cv2.imshow("image", img)

    if(cv2.waitKey(1) == ord("q")):
        break

cap.release()
cv2.destroyAllWindows()
