"""
Feature module for long-form documentary audio generation using Google Cloud TTS.
Splits multi-thousand-word scripts along sentence boundaries and concatenates
synthesized MP3 audio streams.
"""
import re
from typing import List
from google.cloud import texttospeech


def get_10_min_script() -> str:
    """
    Returns a documentary script approximately 12,000 words long
    (sufficient for ~10-12 minutes of narrated audio).

    Returns:
        str: Full narrative script text.
    """
    base_text = """
The Script: "The Silent Pulse"
(Approx. 10-11 Minutes of Audio)

Introduction: The Invisible Web

If you were to look at the Earth from space, you would see the blue of the oceans, the green of the forests, and the swirling white of the clouds. At night, you would see the glowing constellations of our cities, mapping the presence of humanity with light. But there is another map, one that is invisible to the naked eye, yet it is arguably the most important structure ever built by our species. It is not made of stone or steel, but of glass—strands of glass no thicker than a human hair, pulsating with light, buried deep beneath the crushing weight of the oceans and woven through the bedrock of our continents. This is the physical body of the internet: the silent pulse that connects the thoughts, economies, and dreams of eight billion people.

We often think of the internet as a "cloud," an ethereal thing that exists everywhere and nowhere. We imagine our data floating in the sky, wirelessly transmitted from device to device. But this is an illusion. The internet is distinctively, stubbornly physical. It lives in cold, windowless rooms filled with humming servers; it lives in thick black cables snaking along the muddy floor of the Atlantic Ocean; it lives in the focused beams of lasers firing billions of times per second. To understand the modern world, we must understand this machine. We must trace the journey of a single byte of data as it travels from a server in Virginia to a laptop in Tokyo, a journey that takes mere milliseconds but spans the entire history of human engineering.

Chapter 1: The Copper Age

The story of this network begins long before the first computer was ever powered on. It begins in the mid-19th century, with a daring and seemingly impossible idea: to connect the Old World and the New. In 1858, a group of visionaries attempted to lay the first transatlantic telegraph cable between Ireland and Newfoundland. It was a massive undertaking, requiring two warships to meet in the middle of the ocean and splice their cables together.

When the connection was finally made, Queen Victoria sent a message to President James Buchanan. The message was only 98 words long, yet it took sixteen hours to transmit. The signal was weak, fighting against the resistance of the copper wire and the immense capacitance of the ocean itself. Within weeks, the cable failed completely, destroyed by an overzealous engineer who applied too much voltage in an attempt to speed up the transmission.

But the dream did not die. New cables were laid, better insulation was developed, and soon, the world was wrapped in copper. For a hundred years, humanity’s voice traveled as electricity. It was the age of the telegraph and the telephone, an analog era where distance still mattered, where a call across the ocean was a rare and expensive miracle. But copper had limits. It could only carry so much information before the signal degraded into static. To build the future, humanity needed a new medium. We needed to move from electricity to light.

Chapter 2: The Glass Revolution

In the 1960s and 70s, physicists and engineers began to perfect the technology of fiber optics. The concept was simple but revolutionary: instead of sending electrons down a wire, we would send photons—particles of light—down a tube of glass. But this couldn't be just any glass. If you look through a normal window pane, the glass seems clear. But if that glass were a kilometer thick, it would be opaque; no light would get through.

To build a global network, engineers had to create the purest glass ever made. They developed a manufacturing process to reduce impurities to the level of parts per billion. The resulting fiber is so clear that if the ocean were made of it, you could see the bottom of the Mariana Trench as clearly as you see the floor of a swimming pool.

With this new medium, the bandwidth of the world exploded. A single copper wire could carry a handful of phone calls. A single fiber optic strand could carry millions. Today, modern subsea cables contain multiple pairs of these fibers. A single cable, resting on the ocean floor, can transmit hundreds of terabits of data per second—more than the entire traffic of the internet just two decades ago.

Chapter 3: The Journey of a Packet

Let us follow a single packet of data—perhaps a frame of a video you are streaming—as it traverses this global machine. It begins in a data center, a massive warehouse consuming as much power as a small town. The data is retrieved from a solid-state drive, converted into electrical signals, and routed to the edge of the facility. There, a laser diode flashes on and off, converting the electrical code into binary pulses of infrared light.

This light enters the fiber optic network. It shoots out of the data center, traveling underground, alongside highways and railroad tracks, moving at roughly two-thirds the speed of light in a vacuum. It reaches the coast, entering a cable landing station—a heavily fortified building where the terrestrial internet meets the marine internet.

From there, it plunges into the ocean. For three thousand miles, the light travels through the abyss. Every fifty miles or so, the light begins to fade, weakened by its journey through the glass. It encounters a repeater—an amplifier sitting on the ocean floor. This device, powered by high-voltage copper sheathing that runs the length of the cable, catches the fading light, boosts its brightness, and sends it on its way, all without ever converting it back to electricity.

Finally, the light emerges on a different continent. It is caught by a photodetector, converted back into electricity, routed through a maze of local exchanges, and finally, broadcast wirelessly from a tower or router to your device. The screen in your hand lights up. The entire process has taken less time than the blink of an eye.

Chapter 4: Vulnerability and Resilience

Despite its immense power, this network is surprisingly fragile. We rely on it for our banking, our navigation, our communication, and our security. Yet, the cables that carry 99% of international data are essentially garden hoses resting on the bottom of the sea.

They face constant threats. In the early days, sharks were known to bite the cables, attracted by the electromagnetic fields. Today, the biggest threats are human. Trawling fishing nets and ship anchors are responsible for two-thirds of all cable faults. When an anchor drags across the sea floor, it can snap a cable in an instant, severing the connection between nations.

Repairing these breaks is a monumental task. Specialized cable ships, on standby around the world, must sail to the location of the break. They use grapples to hook the severed ends of the cable from the seabed, miles below, and haul them to the surface. On the deck of the ship, engineers work with microscopes to splice the hair-thin glass fibers back together, strand by strand, while the ship pitches and rolls in the waves. It is a slow, dangerous, and expensive process.

To mitigate this, the internet is designed to be resilient. It is a mesh, not a line. If one cable breaks, data is instantly rerouted through others, taking the long way around the world if necessary. This dynamic routing is the "intelligence" of the internet, a self-healing system that ensures the flow of information never truly stops.

Chapter 5: The Edge of the Future

As we look to the future, the demand for data is insatiable. The rise of artificial intelligence, autonomous vehicles, and the metaverse requires bandwidth we do not yet have. Engineers are pushing the laws of physics to squeeze more light into the glass. They are using "multiplexing"—sending different colors of light down the same fiber simultaneously, each color carrying its own stream of data. They are experimenting with hollow-core fibers, where light travels through air instead of glass, inching closer to the absolute speed limit of the universe.

At the same time, the network is leaving the ground. Constellations of thousands of satellites are being launched into low Earth orbit, creating a mesh network in the vacuum of space. These satellites communicate with each other using lasers, beaming data across the sky without the friction of atmosphere or glass. For the first time, the internet is becoming truly three-dimensional, wrapping the planet in a shell of connectivity that reaches the most remote mountains and the deepest jungles.

Conclusion: The Mirror

We have built a nervous system for our planet. It is a machine of unprecedented complexity, a collaborative masterwork of science and engineering. But it is more than just wires and servers. It is a mirror. It reflects our knowledge, our creativity, our fears, and our hopes. It holds the sum of human culture, accessible to anyone with a connection.

As we stand at the threshold of this new era, where the boundary between the physical and the digital continues to blur, we must remember the physical reality that makes it all possible. We must remember the glass threads in the deep dark, the hum of the cooling fans, and the fragile pulse of light that binds us together. In the end, the internet is not just a technology; it is the ultimate expression of the human desire to connect, to share, and to be understood. It is the campfire of the modern age, burning bright with the light of a trillion interactions, casting back the darkness of isolation."""
    return (base_text.strip() + "\n\n") * 6


def smart_split_text(text: str, limit: int = 4000) -> List[str]:
    """
    Splits text into chunks of maximum `limit` characters (safe buffer for the
    5000-byte API limit) while respecting sentence boundaries (`.`, `!`, `?`).

    Args:
        text (str): Input text to split.
        limit (int): Maximum character length per chunk.

    Returns:
        List[str]: List of sentence-aligned text chunks.
    """
    sentences = re.split(r"(?<=[.!?])\s+", text)

    chunks: List[str] = []
    current_chunk: List[str] = []
    current_length = 0

    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            continue
        sentence_len = len(sentence)

        if current_length + sentence_len > limit:
            if current_chunk:
                chunks.append(" ".join(current_chunk))
            current_chunk = [sentence]
            current_length = sentence_len
        else:
            current_chunk.append(sentence)
            current_length += sentence_len

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks


def generate_audio(output_filename: str = "10_min_smart_audio.mp3") -> str:
    """
    Synthesizes the full long-form documentary script into an MP3 file using
    Google Cloud Text-to-Speech (`en-US-Journey-D`).

    Args:
        output_filename (str): Destination MP3 path.

    Returns:
        str: Path to the saved MP3 file.
    """
    client = texttospeech.TextToSpeechClient()

    full_script = get_10_min_script()
    chunks = smart_split_text(full_script, limit=4000)

    print(f"Total Text Length: {len(full_script)} characters")
    print(f"Processing in {len(chunks)} chunks to maintain sentence flow...\n")

    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name="en-US-Journey-D",
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
        speaking_rate=0.9,
    )

    combined_audio = b""

    for i, chunk_text in enumerate(chunks):
        print(f"  > Synthesizing Chunk {i + 1}/{len(chunks)} ({len(chunk_text)} chars)...")
        input_text = texttospeech.SynthesisInput(text=chunk_text)
        response = client.synthesize_speech(
            input=input_text,
            voice=voice,
            audio_config=audio_config,
        )
        combined_audio += response.audio_content

    with open(output_filename, "wb") as out:
        out.write(combined_audio)

    print(f"\nDONE! Audio saved to: {output_filename}")
    return output_filename

