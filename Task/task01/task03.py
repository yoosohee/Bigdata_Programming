#다음 코드의 실행 결과는?

class FourCal:
  def setdata(self, fir, sec):
    self.fir = fir
    self.sec = sec
  def add(self):
    result = self.fir + self.sec
    return result

a = FourCal()
a.setdata(4, 2)
print(a.add())