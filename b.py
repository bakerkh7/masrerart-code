import os
import time
from datetime import datetime

# قائمة عناوين الأجهزة والخوادم الأساسية في شركة MasterArt & Code
targets = {
    "Management VLAN Gateway": "192.168.10.1",
    "Media & Art Department PC": "192.168.20.20",
    "Developers Department PC": "192.168.30.30",
    "Server Gateway": "192.168.99.1"
}

def check_network():
    print(f"=== [MasterArt & Code] تقرير فحص الشبكة - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===")
    
    for name, ip in targets.items():
        # تنفيذ أمر الـ Ping (الباراميتر -n في ويندوز أو -c في لينكس)
        response = os.system(f"ping -n 1 {ip} >nul 2>&1")
        
        if response == 0:
            print(f"[✔ متصل] {name} ({ip}) -> الحالة: تعمل بكفاءة")
        else:
            print(f"[✖ انقطاع] {name} ({ip}) -> تنبيه: لا يمكن الوصول للجهاز!")
            
    print("-" * 60)

if __name__ == "__main__":
    # تشغيل الفحص بشكل دوري
    while True:
        check_network()
        # الانتظار لمدة 10 ثوانٍ قبل الفحص التالي
        time.sleep(10)