import pyttsx3

text = """Voyager 1 and Voyager 2 are NASA's iconic twin spacecraft launched in 1977 to explore the outer planets and now serve as humanity’s farthest-reaching interstellar ambassadors.​

Basic Overview
Voyager 2 launched first on August 20, 1977, followed by Voyager 1 on September 5, 1977 from Cape Canaveral, Florida.​

Both spacecraft were built to last five years but have operated for nearly 48 years, continuing to transmit data from interstellar space.​

Each carries the Golden Record — a phonograph record containing 115 images, greetings in 55 languages, and music from Earth as a message to extraterrestrial life.​

Voyager 1 Facts
Mission Path: Visited Jupiter (1979) and Saturn (1980); its flyby of Saturn’s moon Titan sent it out of the ecliptic plane.​

Interstellar Entry: Entered interstellar space on August 25, 2012, becoming the first human-made object to do so.​

Current Status (2025): Traveling at about 3.6 AU per year (~61,000 km/h) and remains the most distant human-made object, over 24 billion km from Earth.​

Key Discoveries:

Detailed images of Jupiter’s atmosphere and lightning on Saturn.

Discovery of volcanic activity on Io, Jupiter’s moon.​

Direction: Heading toward the constellation Ophiuchus.​

Voyager 2 Facts
Mission Path: Only spacecraft to visit all four giant planets — Jupiter (1979), Saturn (1981), Uranus (1986), and Neptune (1989).​

Unique Discoveries:

Found 14th moon of Jupiter, 10 new moons and 2 rings around Uranus, and 5 moons and 4 rings around Neptune, including the “Great Dark Spot” storm system.​

Interstellar Entry: Joined Voyager 1 in interstellar space on November 5, 2018, crossing the heliopause at about 120 AU from the Sun.​

Current Status (2025): Around 139 AU (20.8 billion km) from Earth, moving at 15.3 km/s, still sending interstellar plasma data via NASA’s Deep Space Network in Canberra.​

Direction: Traveling below the ecliptic toward the constellation Pavo."""
engine = pyttsx3.init()
engine.save_to_file(text, 'Recording.wav')
engine.runAndWait()
