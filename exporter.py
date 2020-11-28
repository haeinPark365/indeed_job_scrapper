
import csv

def save_to_file(jobs):
  print("실행시작")
  file = open("jobs.csv", mode ="w", encoding = "utf-8", newline='')
  #open할 파일명에 해당하는 파일이 없을경우 새로생성
  #mode를 w로 해주면 파일을 덮어씌움 (원래내용 없어짐)
  writer = csv.writer(file)
  writer.writerow(["title", "company", "location", "link"])
  for job in jobs:
    writer.writerow(list(job.values()))
  return