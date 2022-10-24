# MIDIFreak: software MIDI-filter for MicroFreak.

MIDIFreak is a small cross-platform tool that filters the MIDI-clock messages transmitted by the Arturia MicroFreak in arpeggiator and sequencer modes. It seems to you've probably also been demotivated by MicroFreak's MIDI-clock behavior when using it with DAW. It's time to fix it.

You can read more about this issue on the Arturia forum:<br />
https://forum.arturia.com/index.php?topic=101089.0<br />
https://forum.arturia.com/index.php?topic=106599.0<br />
https://forum.arturia.com/index.php?topic=95274.0<br />

[![screenshot.png](https://i.postimg.cc/W1J8gpCT/screenshot.png)](https://postimg.cc/RW4wzmvD)

## Installation steps.
***This tool was tested on Windows 10 (21H1) and MacOS Big Sur 10.6 with Python 3.10.8***

0. Get actual Python version from official site - https://www.python.org/downloads/ <br />
1. Set-up virtual MIDI interface by this guide - https://dialogaudio.com/modulationprocessor/guides/virtual_midi/virtual_midi_setup.php <br />
2. Go to PowerShell (Win) or Terminal (MacOS) and type: <br />
	`git clone https://github.com/SyntheticJudah/midifreak.git`<br />
	`cd midifreak`<br />
	`pip install -r requirements.txt`<br />
	`python midifreak.py`<br />
	***In some cases you need to use "pip3" instead "pip" and "python3" instead "python"*** <br />
3. Select midi in port (your MicroFreak) and midi out port (virtual MIDI) and press start <br />
4. Enjoy! <br />

## If you find this tool useful - you can buy me a coffee :)

Bitcoin - bc1qffgs2rpr444vnszttp58kqtjd3meflm5fgwj8c<br />
Ethereum - 0x79CD0a605eD3B405566cD8913EAff22e055f43B9<br />
Litecoin - ltc1qd0g0r6dg60hvawdw9kussxkd698r69q55u8gfs<br />
Dogecoin - D7jjbvn9A8JFAfyeZXqwkUebjzz3BZEg5B<br />


