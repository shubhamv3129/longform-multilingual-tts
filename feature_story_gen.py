"""
Feature module for generating story audio using Gemini TTS.
Handles text chunking and Google Cloud Text-to-Speech API interactions.
"""
import re
from google.cloud import texttospeech_v1beta1 as texttospeech

def get_full_story_content() -> str:
    """
    Returns the full Hindi story content to be synthesized.
    
    Returns:
        str: The story text.
    """
    return """
    ब्रिंडलब्रुक गांव में रहने वाली बारह साल की लीना विलो के लिए वह रात बिल्कुल सामान्य शुरू हुई थी। लेकिन जब उसने अपनी खिड़की से बाहर देखा, तो आसमान में कुछ ऐसा हो रहा था जो उसने कभी नहीं देखा था। सैकड़ों तारे आसमान से गिर रहे थे, जैसे कोई जादूगर ने अपनी जादू की छड़ी हिलाई हो। लीना का दिल तेज़ी से धड़कने लगा। "यह सामान्य नहीं है... यह कोई संकेत है," वह फुसफुसाई। उसकी आंखों में चमक थी, जैसे वह जानती हो कि कुछ अद्भुत होने वाला है।
    
    जंगल में, गिरे हुए तारों के बीच, लीना को एक चमकती हुई छड़ी मिली। जब उसने उसे उठाया, तो अचानक एक आवाज़ आई, "आह! इतनी कसकर मत पकड़ो!" लीना चौंक गई। छड़ी बोल रही थी! "बिल्कुल! मैं व्हिम्सी हूं, फुसफुसाने वाली छड़ी। और तुम, भाग्यशाली लड़की, मेरी नई रक्षक हो।" तभी एक छोटा सा प्राणी प्रकट हुआ। "मैं टिफो हूं, छड़ी का गाइड। और तुम भयानक खतरे में हो।" उसकी आवाज़ में चिंता थी। "हां, हां, हां! क्योंकि तारे गलती से नहीं गिरे। उन्हें धकेला गया है।"
    
    टिफो ने लीना को उल्टी-सीधी जंगल में ले जाया, जहां पेड़ उल्टे लटके हुए थे और फूल हवा में तैरते थे। "जादू असंभव को... संभव बनाता है," टिफो ने समझाया। लेकिन अचानक एक तीन आंखों वाले उल्लू की गहरी आवाज़ गूंजी, "छड़ी की रक्षक... शैडो कलेक्टर तुम्हारे लिए आ रहा है।" लीना की रीढ़ में सिहरन दौड़ गई। यह कोई साधारण चेतावनी नहीं थी। यह एक खतरनाक दुश्मन का संदेश था जो जादू चुराता था।

    जैसे-जैसे लीना, व्हिम्सी और टिफो ने जादुई दुनिया की यात्रा की, वे अद्भुत जगहों से गुज़रे। चांदी के झरने, बात करने वाले पेड़, और इंद्रधनुषी पुल। लेकिन हर कदम पर, शैडो कलेक्टर का डर उनके साथ था। वह एक काला, लंबा आकार था जो बच्चों से उनका जादू छीन लेता था। "मुझे छड़ी दे শর্মা दो... या अपना जादू हमेशा के लिए खो दो," उसकी आवाज़ हवा में गूंजती थी।
    
    लेकिन लीना डरी नहीं। उसके अंदर कुछ था जो उसे आगे बढ़ने के लिए प्रेरित कर रहा था। स्टारफॉल वैली में, आखिरकार वह पल आया जिसका इंतज़ार था। शैडो कलेक्टर सामने खड़ा था, विशाल और डरावना। "फुसफुसाने वाली छड़ी मुझे दे दो। जादू बच्चों के लिए नहीं है," उसने गरजकर कहा। लेकिन लीना ने हिम्मत जुटाई। "जादू उसका है जो इसमें विश्वास करता है," उसने दृढ़ता से कहा। व्हिम्सी ने फुसफुसाया, "रक्षक... प्राचीन शब्द कहो।"
    
    लीना ने गहरी सांस ली और चिल्लाई, "प्रकाश उठे। छाया गिरे। जादू सबके पास वापस आए।" एक चमकदार रोशनी फूटी और शैडो कलेक्टर पिघलकर गायब हो गया। तारे वापस आसमान में चमकने लगे। टिफो ने गर्व से कहा, "आज से, लीना विलो... तुम आश्चर्य की रक्षक हो।"
    
    लेकिन लीना के लिए यह सिर्फ शुरुआत थी। उसने फैसला किया कि वह अपने गांव के हर बच्चे के साथ जादू साझा करेगी। "जादू को अब छुपाने की ज़रूरत नहीं। इसे साझा करने की ज़रूरत है," उसने कहा। वह बच्चों को सिखाने लगी कि सामान्य चीज़ों में भी आश्चर्य कैसे खोजा जाए। "क्योंकि जादू... वहीं रहता है जहां बच्चे की कल्पना रहती है।" और इस तरह, ब्रिंडलब्रुक गांव हमेशा के लिए बदल गया, जहां हर बच्चा जानता था कि जादू सच में मौजूद है।
    """

def smart_split_text(text: str, limit: int = 1000) -> list:
    """
    Splits text into chunks by sentences, ensuring no chunk exceeds the limit.
    
    Args:
        text (str): The text to split.
        limit (int): The maximum character limit per chunk.
        
    Returns:
        list: A list of text chunks.
    """
    sentences = re.split(r'(?<=[.|\n])\s+', text)
    chunks = []
    current_chunk = []
    current_length = 0
    
    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence: 
            continue
        
        sent_len = len(sentence)
        
        if current_length + sent_len > limit:
            chunks.append(" ".join(current_chunk))
            current_chunk = [sentence]
            current_length = sent_len
        else:
            current_chunk.append(sentence)
            current_length += sent_len
            
    if current_chunk:
        chunks.append(" ".join(current_chunk))
    return chunks

def generate_gemini_audio() -> None:
    """
    Generates an MP3 audio file from the story text using Google Cloud Text-to-Speech
    with the 'gemini-2.5-pro-tts' model.
    """
    client = texttospeech.TextToSpeechClient()
    
    full_text = get_full_story_content()
    chunks = smart_split_text(full_text, limit=1000) 
    
    voice_params = texttospeech.VoiceSelectionParams(
        language_code="hi-IN",
        name="Algenib",
        model_name="gemini-2.5-pro-tts"
    )
    
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
        sample_rate_hertz=24000,
        speaking_rate=1.0
    )

    output_filename = "Gemini_Hindi_Final.mp3"
    
    print(f"Generating audio in {len(chunks)} chunks using model 'gemini-2.5-pro-tts'...")

    with open(output_filename, "wb") as f:
        for i, chunk in enumerate(chunks):
            print(f"  > Processing Chunk {i+1} ({len(chunk)} chars)...")
            
            request = texttospeech.SynthesizeSpeechRequest(
                input=texttospeech.SynthesisInput(text=chunk),
                voice=voice_params,
                audio_config=audio_config
            )

            try:
                response = client.synthesize_speech(request=request)
                f.write(response.audio_content)
            except Exception as e:
                print(f"    CRITICAL ERROR on chunk {i+1}: {e}")
                print(f"    (The file might be incomplete)")
                return 

    print(f"\nSUCCESS! Audio saved to: {output_filename}")
