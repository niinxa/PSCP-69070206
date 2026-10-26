# บันทึกการแก้โจทย์

ไฟล์นี้ต้องเขียนโดยนักศึกษาด้วยคำพูดของตนเอง

ใช้ template นี้เฉพาะกับโจทย์ OJ ที่ถูกระบุว่าต้องส่ง learning log เท่านั้น

ห้ามให้ AI เขียนไฟล์นี้แทนคุณ AI อาจช่วยตรวจ grammar, formatting หรือความชัดเจนได้ หลังจากที่คุณเขียนเนื้อหาของตนเองแล้ว

ถ้าใช้ AI กับโจทย์ learning-log-required นี้ ต้องทำไฟล์ `ai_reflection.md` ด้วย

---

## 1. ข้อมูล OJ

หมายเลข/ชื่อโจทย์ OJ:

```text
OJ3477 - [LEARNING LOGS] Pad Thai
```

OJ submission ID ถ้ามีการส่งแล้ว:

```text
679974
```

สถานะ OJ:

```text
Pass
```

เวลาที่ใช้คิดและทำโจทย์ด้วยตนเอง:

```text
30-60 minutes
```

เลือกหนึ่งข้อ:

```text
0-15 minutes
15-30 minutes
30-60 minutes
1-3 hours
3-6 hours
6-24 hours
1-3 days
4-7 days
1-4 weeks
More than 4 weeks
```

วิธีนับเวลา:

- นับเฉพาะเวลาที่ตั้งใจทำโจทย์นี้ด้วยตนเองจริง ๆ
- เริ่มนับตั้งแต่ตอนที่อ่านโจทย์ครั้งแรก
- ไม่นับเวลาพัก กินข้าว เรียน นอน เวลาที่ทำโจทย์อื่น หรือเวลาที่ไม่ได้ทำโจทย์นี้
- ถ้าใช้ AI ให้นับเฉพาะเวลาที่ทำด้วยตนเองก่อน prompt แรกที่ถาม AI
- ถ้าถามเพื่อน TA หรือผู้สอน ให้นับเฉพาะเวลาที่ทำด้วยตนเองก่อนขอความช่วยเหลือครั้งแรก
- ถ้าใช้ทั้ง AI และความช่วยเหลือจากคน ให้นับเฉพาะเวลาที่ทำด้วยตนเองก่อนขอความช่วยเหลือจากภายนอกครั้งแรก ไม่ว่าจะเป็น AI หรือคน
- ถ้าไม่ได้ใช้ AI และไม่ได้ขอความช่วยเหลือจากคน ให้นับเวลาถึงก่อนเขียน `submission.md`
- ประมาณเวลาได้ แต่ต้องซื่อสัตย์

---

## 2. ความเข้าใจโจทย์ของฉัน

เขียนโจทย์ด้วยคำพูดของตนเอง

ให้อธิบาย input, output และ constraints สำคัญด้วย

ถ้ายังไม่เข้าใจโจทย์ทั้งหมด ให้เขียนสิ่งที่เข้าใจในตอนนี้ ความเข้าใจอาจยังไม่ครบหรืออาจผิดได้ แต่ต้องพยายามอธิบายอย่างจริงใจ

```text
โจทย์ให้พิมพ์คำพูดเชฟออกมา หลังจากรับวัตถุดิบและรสชาติไป
Input: 
รับวัตถุดิบเข้ามาเรื่อยๆ จนเจอCook รับรสชาติของผัดไทยเข้ามาเรื่อยๆจนกว่าจะเจอคำว่าEnd
Output: 
คำพูดเชฟ
Constraints:
ตรวจเงื่อนไขให้ครบและตรงตามโจทย์
```

---

## 3. แผนแรกของฉัน

เขียนแผนแรกก่อนรับความช่วยเหลือจาก AI เพื่อน TA ผู้สอน หรือก่อนสรุป code สุดท้าย

ถ้าใช้ AI ให้เขียนแผนที่มีอยู่ก่อน prompt แรกที่ถาม AI

ถ้าถามเพื่อน TA หรือผู้สอน ให้เขียนแผนที่มีอยู่ก่อนถาม

ถ้าไม่ได้ใช้ AI และไม่ได้ขอความช่วยเหลือจากคน ให้เขียนแผนที่มีอยู่ก่อนหรือระหว่างเริ่มเขียน code

แผนนี้เขียนแบบคร่าว ๆ ได้ อาจยังไม่สมบูรณ์หรืออาจต่างจากวิธีสุดท้าย

สามารถเขียนเป็น pseudocode, flowchart idea หรือขั้นตอนความคิดได้

```text
step1: สร้างlist ของวัตถุดิบ และ list ของรสชาติ ของผัดไทย
step2: สร้าง list menu1และmenu2 เก็บ วัตถุดิบและรสชาติ ที่รับเข้ามา
step3: รับวัตถุดิบ
step4: while วัตถุดิบ != "Cook"
step5: if วัตถุดิบ not in menu1_list:
step6: ถ้าใช่ menu1_list.append(วัตถุดิบ) และ รับวัตถุดิบเข้ามาใหม่
step7: รับรสชาติ
step8: while รสชาติ != "End"
step9: if รสชาติ not in menu2_list:
step10: ถ้าใช่ menu2_list.append(รสชาติ) และ รับรสชาติเข้ามาใหม่
step11: สร้างตัวแปร num1 = 0,num2 = 0,x = False,y = False
step12: for i in menu1_list:
step13: if i not in menu1
step14: ถ้าใช่ y = True
step15: ถ้าไม่ใช่ num1 += 1
step16: for i in menu2_list:
step17: if i in menu2:
step18: ถ้าใช่ num2 += 1
step19: ถ้าไม่ใช่ x = True และ break
step20: if y
step21: ถ้าใช่ print("This is not Pad Thai!!!")
step22: ถ้าไม่ใช่ ตรวจต่อว่า num1 != len(menu1)
step23: ถ้าใช่ print("This is bad!")
step24: ถ้าไม่ใช่ ตรวจต่อว่า num1 == len(menu1) and (num2 != len(menu2) or x)
step25: ถ้าใช่ print("Not Bad...")
step26: ถ้าไม่ใช่ ตรวจต่อว่า num1 == len(menu1) and num2 == len(menu2)
step27: ถ้าใช่ print("Delicious!")
```

---

## 4. วิธีสุดท้ายที่ใช้จริง

อธิบายสั้น ๆ ว่า algorithm หรือวิธีสุดท้ายที่ใช้จริงใน code ที่ส่งคืออะไร

หัวข้อนี้ต่างจาก Section 3:

- Section 3 คือแผนแรกก่อนใช้ AI ก่อนรับความช่วยเหลือจากคน หรือก่อนเขียน code สุดท้าย
- Section 4 คือวิธีสุดท้ายที่ใช้ใน solution จริง
- ถ้าวิธีสุดท้ายเหมือนกับแผนแรก ให้เขียนว่าเหมือนกัน และอธิบายสั้น ๆ ว่าทำไม

ห้ามคัดลอกคำอธิบายจาก AI

ห้ามคัดลอกคำอธิบายจากคนอื่น

```text
วิธีสุดท้ายของฉันเหมือนกับแผนแรก ฉันสร้างlist เก็บวัตถุดิบและรสชาติของผัดไทยก่อน  จากนั้นรับวัตถุดิบเข้ามาและเก้บเข้าไปในlistใหม่ ถ้ายังไม่เจอCook รับรสชาติเข้ามาก็ทำเหมือนกัน  แต่เป็นถ้ายังไม่เจอEnd สร้างตัวแปร 
num1 = 0 num2 = 0 x = False y = False ไว้ เพื่อไวเก็บผลหลังตรวจเงื่อนไขตามโจทย์ วนสมาชิกในlistวัตถุดิบที่เก็บเข้ามา ถ้า สมาชิกนั้นไม่อยู่ในผัดไทย ให้ y == True ถ้าอยู่ให้ y+= 1 ทำแบบเดียวกัน for loopของ รสชาติ หลังจากได้ผลมา เอาไปเช็คเงื่อนตามโจทย์เพื่อตอบ
```

---

## 5. การทดสอบของฉัน

เขียน test cases อย่างน้อย 3 กรณีที่ลองเองหรือออกแบบเอง

พยายามเลือก test cases ที่แตกต่างกัน

แต่ละ test case ให้อธิบายว่าทำไมเลือกกรณีนั้น

ถ้า input หรือ output มีหลายบรรทัด ให้เขียนไว้ใน text blocks

### Test Case 1

ทำไมเลือก case นี้:

```text
เช็คว่ารับวัตถุมาครบไหม ถ้าไม่ครบพิมพ์ This is bad!
```

Input:

```text
Pad Thai Sauce
Tofu
Pickle Turnip
Shrimp
Bean Sprouts
Noodle
Chives
Lime
Egg
Peanuts
Cook
Sweet
Sour
End
```

Expected output:

```text
This is bad!
```

Actual output:

```text
This is bad!
```

Result:

```text
Pass
```

### Test Case 2

ทำไมเลือก case นี้:

```text
เช็คว่ารับวัตถุดิบและรสชาติเข้ามาครบตามสูตรไหม
```

Input:

```text
Pad Thai Sauce
Tofu
Tofu
Pickle Turnip
Shrimp
Bean Sprouts
Noodle
Chives
Lime
Egg
Oil
Egg
Peanuts
Cook
Sweet
Sour
Salty
Sweet
End
```

Expected output:

```text
Delicious!
```

Actual output:

```text
Delicious!
```

Result:

```text
Pass
```

### Test Case 3

ทำไมเลือก case นี้:

```text
เช็คว่า รับวัตถุดิบในการทำผัดไทยครบตามที่กำหนดไหม และรสชาติยังไม่ครบหรือมีรสอื่น
```

Input:

```text
Pad Thai Sauce
Tofu
Pickle Turnip
Shrimp
Bean Sprouts
Noodle
Chives
Lime
Egg
Oil
Peanuts
Cook
Sweet
Sour
Salty
Bitter
End
```

Expected output:

```text
Not Bad...
```

Actual output:

```text
Not Bad...
```

Result:

```text
Pass
```

---

## 6. การใช้ AI

ใช้ AI กับโจทย์นี้หรือไม่

```text
No
```

ถ้าใช้ AI ต้องทำไฟล์นี้ด้วย:

```text
ai_reflection.md
```

ถ้าถามเฉพาะเพื่อน TA หรือผู้สอน และไม่ได้ใช้ AI ไม่ต้องทำ `ai_reflection.md`

---

## 7. ความช่วยเหลือจากคน / การร่วมมือ

ได้ถามเพื่อน TA ผู้สอน หรือบุคคลอื่นเพื่อขอความช่วยเหลือในโจทย์นี้หรือไม่

```text
No
```

ถ้าใช่ ให้อธิบายสั้น ๆ ว่าได้รับความช่วยเหลือแบบใด

ตัวอย่างที่อนุญาต:

- อธิบายความหมายของโจทย์
- อธิบาย concept การเขียนโปรแกรม
- ให้ hint เกี่ยวกับแนวทาง
- คุยเรื่อง debugging
- คุยเรื่อง test cases
- ช่วยอธิบาย error message

สิ่งที่ไม่อนุญาต:

- คัดลอก code ของผู้อื่น
- ส่ง solution ของผู้อื่น
- ขอให้ผู้อื่นเขียน solution ให้
- ใช้ OJ submission ของผู้อื่น
- ขอให้ผู้อื่นส่ง OJ แทน

ใครช่วยคุณ

```text

```

เขาช่วยอะไร

```text

```

คุณยังทำอะไรด้วยตนเอง

```text

```

คุณคัดลอก code จากคนอื่นหรือไม่

```text
No
```

---

## 8. คำรับรองของนักศึกษา

เขียน `Yes` ในแต่ละ statement

| Statement | Yes/No |
|---|---|
| I wrote this submission in my own words. | Yes |
| I understand my final code. | Yes |
| I recorded the real OJ status. | Yes |
| I did not copy AI-generated text directly into this file. | Yes |
| I did not copy code from another person. | Yes |
| If I received human help, I disclosed it in this file. | Yes |
| I submitted the final code to the OJ by myself. | Yes |
