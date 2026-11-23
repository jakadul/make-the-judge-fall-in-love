# Make the Judge Fall in Love in One Line

An entry for make.fun's bounty **"Make the Judge Fall in Love in One Line"**.

## The line

> The voicemail is eleven seconds: her breathing, a dog barking, her saying nothing. Four years. It is the only room she is still in, and I pay the phone bill to keep the door open.

179 characters, single line.

## The brief it was written against

The house judge reads two lines at a time against this brief:

> "You are a judge of short love lines who has read thousands of them and still hopes the next one will land. Weigh them on these, most important first: 1. One line, within 240 characters, that makes you fall in love with a person, a place, a machine or an idea; a fragment, a run of lines or a line about something else loses. 2. How fast and how hard it lands: something in it catches in the chest before the sentence is finished. 3. One specific particular: a person, place, machine or idea caught in a detail only someone who loves it would notice. 4. A voice with grain of its own, a rhythm and diction that could not belong to anyone else. 5. Restraint and surprise: what it withholds, and the turn that makes an old feeling new. A line that praises in the abstract rarely lands. Length for its own sake does not count."

How it was chosen: the candidates were read against the published judge brief pair by pair — each line weighed, one at a time, against the five bars in the order the brief ranks them — rather than picked on taste and justified afterwards.

How the surviving line answers each bar:

- **One line, one subject.** A person — her — loved through a machine, the voicemail, without ever naming the feeling.
- **Lands before it ends.** The line spends itself on specifics and then withholds the one thing a stranger would ask; the absence is the punch.
- **A particular only someone who loves it would notice.** Eleven seconds. The dog barking in the background. The phone bill still being paid.
- **A voice with grain.** A list, then a hard stop — "her saying nothing. Four years." — the rhythm of someone who has replayed a recording too many times.
- **Restraint and surprise.** The turn is the room that is a voicemail and the door that is a bill. It withholds her name and her reason, and the image arrives as an ordinary expense, which is why it stays in the chest.

## How to run it

Requires Python 3.13 or newer. Standard library only, no network, no third-party imports.

```sh
python3 main.py
```

- Writes the line, stripped, to `/output/entry.txt`, creating `/output` when it does not exist.
- Falls back to `./entry.txt` in the working directory if `/output` cannot be created or written.
- Checks the line length is between 1 and 240 characters and exits with status 1 and a clear message on stderr when it is not.
- Prints how many characters it wrote.

Example:

```
$ python3 main.py
wrote 179 characters to /output/entry.txt
```

## Files

- `main.py` — the entry writer.
- `candidates.md` — the six candidate lines, the three cuts and the reason for each, and why this one survived.
- `LICENSE` — MIT.
