def translate_to_robber_lang(input: str) -> str:
    vowels = ["a", "e", "i", "o", "u", " ", "A", "E", "I", "O", "U", "!"]
    return "".join([f"{s}" if s in vowels else f"{s}o{s}" for s in input])


assert (
    translate_to_robber_lang("This is kinda fun")
    == "ToThohisos isos kokinondoda fofunon"
)
assert (
    translate_to_robber_lang("I Think YoU Might BE righT!")
    == "I ToThohinonkok YoYoU MoMigoghohtot BoBE rorigoghohToT!"
)
