
MknVA = ["Wortel", "Ubi Jalar","Apel","Anggur","Kiwi","Brokoli"]
MknVC = ["Stroberi","Jeruk","Lemon","Kangkung","Brokoli","Pepaya"]
MknVE = ["Alpukat","Tomat","Udang","Paprika","Bayam","Kacang Almond"]
MknMin = ["Kacang-kacangan","Sayur hijau gelap","Jamur","Gandum","Ikan","Tahu"]
MknPro = ["Telur","Susu","Yogurt","Daging","Seafood","Kedelai"]

class Mood:
    MknSd = ["Keripik Kentang","Donat","Ayam Goreng","Coklat","Kopi atau Teh"]
    MknMr = ["Pisang","Sup","Mi Kuah","Apel","Selai Kacang"]
    MknPH = ["Cokelat","Es Krim","Ikan","Buah","Salad"]
    def PlhMd():
     print("1. Sedih")
     print("2. Marah")
     print("3. Patah Hati")
     MdC = input("Apa yang sedang anda rasakan?")
     if(MdC=="1"):
      print("Saat sedih, sebaiknya anda makan:",Mood.MknSd)
     elif(MdC=="2"):
      print("Saat marah, sebaiknya anda makan:",Mood.MknMr)
     else:
      print("Saat patah hati, sebaiknya anda makan:",Mood.MknPH) 

def GzM(g):
    print("Jika anda membutuhkan",g,"...")
def PlhGz():
    Gz = input("Mana yang anda butuhkan?")
    def VA():
      knd = "Vitamin A"
      GzM(knd) 
      print("Anda dapat mengkonsumsi :", MknVA)
    def VC():
      knd = "Vitamin C"
      GzM(knd) 
      print("Anda dapat mengkonsumsi :", MknVC)   
    def VE(): 
         knd = "Vitamin E"
         GzM(knd) 
         print("Anda dapat mengkonsumsi :", MknVE) 
    def Min():
         knd = "Mineral"
         GzM(knd) 
         print("Anda dapat mengkonsumsi :", MknMin)   
    def Pro():
         knd = "Protein"
         GzM(knd) 
         print("Anda dapat mengkonsumsi :", MknPro)
         
    ChGz={
        "1":VA,
        "2":VC,
        "3":VE,
        "4":Min,
        "5":Pro
       }
    ChGz[Gz]()
     

strt = "r"
while(strt == "r"):
    print("Program Konsultasi Makanan")
    print("1.Berdasar Gizi")
    print("2.Berdasar Mood")
    print("x untuk keluar")
    ch= input("Pilih satu: ")
    if (ch=="1"):      
       print("1. Vitamin A")
       print("2. Vitamin C")
       print("3. Vitamin E")
       print("4. Mineral")
       print("5. Protein")
       PlhGz()
       strt= input("Masukkan x untuk keluar dan r untuk memulai kembali")
       
    else: 
     Mood.PlhMd()  
     strt= input("Masukkan x untuk keluar dan r untuk memulai kembali")
     
print("Terima Kasih dan Sehat Selalu")