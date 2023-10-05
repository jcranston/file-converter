import fire

def main():
  in1 = ["3gp", "AVI", "DS_Store", "JPG", "MP4", "MPG", "NEF", "au", "aup",
         "avi", "cxf", "db", "docx", "ini", "jpeg", "jpg", "mov", "mp4", "php",
         "png", "psd", "wmv"]
  in2 = ["DS_Store", "JPG", "jpeg", "jpg"]
  in3 = ["DS_Store", "jpg", "m4v"]

  s = set()
  s.update(in1)
  s.update(in2)
  s.update(in3)

  l = list(s)
  print(l)

if __name__ == '__main__':
  main()