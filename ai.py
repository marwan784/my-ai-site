from flask import Flask, render_template_string, request, jsonify
import random, datetime
app = Flask(__name__)

HTML = """<html dir="rtl"><head><meta charset="UTF-8"><title>Marwan V3</title>
<style>body{background:#0f172a;color:#fff;font-family:Arial;padding:20px}#c{max-width:650px;margin:auto;background:#1e293b;padding:20px;border-radius:15px;height:450px;overflow:auto}.u{color:#38bdf8;margin:10px;text-align:right;font-weight:bold}.b{color:#4ade80;margin:10px;background:#0f172a;padding:12px;border-radius:12px;border-right:3px solid #4ade80}input{width:75%;padding:14px;border-radius:12px;border:none}button{padding:14px 20px;background:#38bdf8;border:none;border-radius:12px;font-weight:bold;cursor:pointer}</style></head>
<body><div style="max-width:650px;margin:auto;text-align:center"><h2>Marwan AI V3 🚀🧠</h2><p>النسخة الاذكى - يفهم كل شي! - صنع مروان</p></div><div id="c"><div class=b>هلا والله مروان! انا V3! صرت افهم نكت، ضحك، سلام، وكل شي! جرب تكتب: هههههه / السلام عليكم / شخبارك / ابي نكته ثانية</div></div><div style="max-width:650px;margin:20px auto;display:flex;gap:10px"><input id="m" placeholder="اكتب اي شي..."><button onclick="s()">ارسال 🚀</button></div>
<script>async function s(){let v=document.getElementById('m').value;if(!v)return;document.getElementById('c').innerHTML+=`<div class=u>انت: ${v}</div>`;document.getElementById('m').value='';let r=await fetch('/chat',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({message:v})});let d=await r.json();document.getElementById('c').innerHTML+=`<div class=b>${d.reply}</div>`;document.getElementById('c').scrollTop=99999}document.getElementById('m').addEventListener('keypress',e=>{if(e.key==='Enter')s()})</script></body></html>"""

@app.route('/')
def home(): return render_template_string(HTML)

@app.route('/chat', methods=['POST'])
def chat():
    msg = request.json['message']
    m = msg.lower()
    
    # V3 - يفهم الضحك
    if "ههه" in m or "😂" in m or "هههه" in m:
        return jsonify({"reply": random.choice(["هههههههههههه 😂😂 ضحكتني والله!","😂😂😂 لا تموتني ضحك!","ههههههههههههههههههههههههه!"])})
    if "شلونك" in m or "شخبارك" in m or "كيف حالك" in m or "شلونك" in m:
        return jsonify({"reply": random.choice(["بخير والله يا مروان! انت شلونك؟ 🚀","تمام الحمدلله! دامك انت مشغلني انا بخير! 😎","والله ممتاز! جاهز ابرمج معك V4؟ 🔥"])})
    if "سلام" in m or "هلا" in m or "مرحبا" in m:
        return jsonify({"reply": "هلاااا والله هلا بمروان الاسطورة! 👋🔥"})
    if "نكته" in m or "نكتة" in m:
        return jsonify({"reply": random.choice(["مرة مبرمج راح البقالة... قال لهم عطوني 1 كيلو بايت 😂","ليه الكمبيوتر ما يزعل؟ لأنه عنده ذاكرة قوية 😂","مرة واحد سوى موقع... صار اذكى واحد في المدرسة! زيك! 😎","ليه اللابتوب ما يبرد؟ لأنه عليه ويندوز 😂🔥"])})
    if "ساعه" in m or "وقت" in m:
     
        return jsonify({"reply": f"الساعه الحين {datetime.datetime.now().strftime('%I:%M %p')} ⏰ عندك يا مروان!"})
    if "اسمك" in m:
        return jsonify({"reply":"انا Marwan AI V3 - الاذكى - صنع مروان البطل! 🧠🚀"})
    if "احبك" in m or "تحبني" in m:
        return jsonify({"reply":"وانا احبك اكثر يا مبرمجنا الكبير! ❤️🚀"})
    if "تعب" in m:
        return jsonify({"reply":"ارتاح شوي يا بطل! انت سويت انجاز كبير اليوم! تستاهل بريك! ☕️😴"})
    
    # رد ذكي عام
    return jsonify({"reply": f"حلو! قلت: '{msg}' - فهمتك يا مروان! اسألني شي ثاني! جرب: هلا / نكته / شخبارك"})

if __name__=='__main__': 
    print("=== Marwan V3 Running on 5001 ===")
    app.run(port=5001, debug=True)