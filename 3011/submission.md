1. ข้อมูล OJ
หมายเลข/ชื่อโจทย์ OJ:

3011 - Colors

OJ submission ID ถ้ามีการส่งแล้ว:

544471

สถานะ OJ:

Pass

เวลาที่ใช้คิดและทำโจทย์ด้วยตนเอง:

30 minutes

เลือกหนึ่งข้อ:

30 - 60 minutes


2. ความเข้าใจโจทย์ของฉัน
โจทย์ให้ผสมแม่สี2ตัว ให้เกิดสีใหม่ แต่ถ้าใช้สีนอกจากแม่สีมาผสม จะเกิดError

input : รับแม่สีมา 2 ข้อความ

Output : สีผ่านการผสม 

Constraints : ถ้าใช้สีนอกจากแม่สีมาผสม จะเกิดError และ ถ้าสีเดียวกันผสมกัน จะะได้สีเดิม

3. แผนแรกของฉัน

step 1: รับinputสี เข้ามา 2 ค่า

step 2: สร้างเงื่อนไขการผสมสี ตามโจทย์

step 3: แสดงผลข้อความ สีที่ผสมกันได้ หรือ Error


4. วิธีสุดท้ายที่ใช้จริง

วิธีสุดท้ายของฉันตือ รับinputมาและแปลงเป็นพิมเล็กทั้งหมด จากนั้นเอาไปตรวจในเงื่อนไขผสมสี ที่สามารถสลับตำแหน่งกันได้ มีเงื่อนไขที่แม่สีเหมือนกันจะได้สีเดิม และถ้าไม่ใช่แม่สีที่เอาผสมจะได้Error


5. การทดสอบของฉัน

Test Case 1

ทำไมเลือก case นี้:

ตรวจว่าผสมสีตามเงื่อนไข แล้วออกมาเป็นสีใหม่ไหม

Input:

Red
Yellow

Expected output:

Orange

Actual output:

Orange

Result:

Pass


Test Case 2

ทำไมเลือก case นี้:

ตรวจว่าถ้าไม่ใช่แม่สีที่เอามาผสม จะเกิดErrorไหม

Input:

Green
Blue

Expected output:

Error

Actual output:

Error

Result:

Pass


Test Case 3

ทำไมเลือก case นี้:

ตรวจว่าถ้าใช้แม่สีเดียวกันมาผสมกัน จะได้สีเดิมไหม

Input:

Red
Red

Expected output:

Red

Actual output:

Red

Result:

Pass


6. การใช้ AI

ใช้ AI กับโจทย์นี้หรือไม่

Yes


7. ความช่วยเหลือจากคน / การร่วมมือ

ได้ถามเพื่อน TA ผู้สอน หรือบุคคลอื่นเพื่อขอความช่วยเหลือในโจทย์นี้หรือไม่

No


8. คำรับรองของนักศึกษา

เขียน Yes ในแต่ละ statement

Statement	Yes/No
I wrote this submission in my own words.	Yes

I understand my final code.	Yes

I recorded the real OJ status.	Yes

I did not copy AI-generated text directly into this file.	Yes

I did not copy code from another person.	Yes

If I received human help, I disclosed it in this file.	Yes

I submitted the final code to the OJ by myself.	Yes
