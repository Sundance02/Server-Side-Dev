from django.db import models

#การเเก้ไขโครงสร้าง db สามารถทำผ่าน models ได้เลย โดยไม่ต้องใช้ query เลยสักคำสั่งเดียว 

# 1 class = 1 ตาราง
# make migrations คือการเทียบตารางใน db กับใน code ของ models.py ว่าตรงกันไหม ถ้าไม่จะเตรียมเเก้ไขลงใน db โดยถ้าไม่ตรงจะทำการสร้างไฟล์ใน โฟลเดอร์ migrations ชื่อว่า 0001_initial.py (เลขจะ run ไปเรื่อยๆตามจำนวนครั้งที่เรา run คำสั่ง make migrations)
# migrate คือการเปลี่ยนเเปลง db ตามที่เรากำหนดไว้


class Question(models.Model): 
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    
    def __str__(self):
        return self.question_text



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text    