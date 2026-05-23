import requests
from pathlib import Path
#test2txt is Снимок экрана 2026-04-06 225916.png
DAY5_DIR = Path(__file__).resolve().parent
class TestFileUploadDownload:
    BASE_URL = "http://localhost:3000"
    FILE1 = DAY5_DIR / "testData" / "foto_1.jpeg"
    FILE2 = DAY5_DIR / "testData" / "foto_2.jpg"


    def test_upload_single_file(self):
        with open(self.FILE1,"rb") as file:
            files = {"file":file}
            res = requests.post(f"{self.BASE_URL}/uploadFile",files=files)
        assert res.status_code == 200, "Upload Failed"
        data = res.json()
        assert data['fileName'] == "foto_1.jpeg", "Wrong file name"
        print(data)

    def test_upload_multiple_file(self):
        with open(self.FILE1,"rb") as f1, open(self.FILE2, "rb") as f2:
            files = [("files",f1), ("files",f2)]
            res = requests.post(f"{self.BASE_URL}/uploadMultipleFiles",files=files)
        assert res.status_code == 200, "Upload Failed"
        data = res.json()
        print(data)
        #ключи.pdf

    def test_download_file(self):
        filename = "foto_1.jpeg"
        with open(self.FILE1, "rb") as file:
            upload = requests.post(
                f"{self.BASE_URL}/uploadFile", files={"file": file}
            )
        assert upload.status_code == 200, "Upload before download failed"
        res = requests.get(f"{self.BASE_URL}/downloadFile/{filename}")
        assert res.status_code == 200, "wrong status code"
        output_path = f"downloaded_{filename}"
        with open(output_path, 'wb') as f:
            f.write(res.content)
        
