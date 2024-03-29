class Plugin:

    def __init__(self, name, category_name):
        ###
        #  plugin name
        self.name = name

        self.new_line = "\n"
        self.double_line = self.new_line+self.new_line
        ###
        #  Name for categories in the database
        self.category_name = category_name

    def parse(self, data):
        raise NotImplementedError

    def handle_entries(self, entries, lines):
        for line in entries:
            # Handle tables
            if type(line) == dict:
                line_type = line["type"]
                if line_type == "list":
                    for list_item in line["items"]:
                        lines += "- {}{}".format(list_item, self.new_line)
                elif line_type == "table":
                    # Caption
                    if not self.format_if_not_none("{}{}{}", lines, [self.new_line, line.get("caption", None),
                                                                     self.new_line]):
                        lines += self.new_line
                    # lines += .format(self.new_line, line["caption"], self.new_line))
                    lines += self.new_line
                    lines += self.new_line
                    # Spacing
                    lines += "|{}|{}".format('|'.join(line["colLabels"]), self.new_line)
                    # Rows
                    lines += "|{}|{}".format("|".join((['-'] * len(line["colLabels"]))), self.new_line)
                    for row in line["rows"]:
                        lines += "|{}|{}".format('|'.join(row), self.new_line)
                elif line_type == "entries":
                    # Super annoying special case, used for curses
                    lines += "{}{}**{}.** ".format(self.new_line, self.new_line, line["name"])
                    for entry in line["entries"]:
                        if type(entry) == str:
                            lines += entry
                        else:
                            self.handle_entries(entry, lines)

            else:
                lines += line
                lines += self.new_line
        return lines

    @staticmethod
    def format_if_not_none(string, lines, attrs):
        if None not in attrs:
            lines += string.format(*attrs)
            return True
        return False

    @staticmethod
    def get_ability(ability):
        if "int" == ability:
            return "Intelligence"
        elif "cha" == ability:
            return "Charisma"
        elif "wis" == ability:
            return "Wisdom"
        elif "str" == ability:
            return "Strength"
        elif "dex" == ability:
            return "Dexterity"
        elif "con" == ability:
            return "Constitution"

    @staticmethod
    def get_property(i_type, is_property):
        byline = ""
        if "A" == i_type:
            byline += "Ammunition"
        elif "AT" == i_type:
            byline += "Artisans Tools"
        elif "AF" == i_type:
            byline += "Ammunition"
        elif "BF" == i_type:
            byline += "Burst Fire"
        elif "EXP" == i_type:
            byline += "Explosive"
        elif "F" == i_type:
            byline += "Finesse"
        elif "G" == i_type:
            byline += "General"
        elif "GS" == i_type:
            byline += "Game Set"
        elif "H" == i_type:
            byline += "Heavy"
        elif "HA" == i_type:
            byline += "Heavy Armour"
        elif "INS" == i_type:
            byline += "Instrument"
        elif "L" == i_type:
            byline += "Light"
        elif "LA" == i_type:
            byline += "Light Armour"
        elif "LD" == i_type:
            byline += "Loading"
        elif "M" == i_type:
            byline += "Melee Weapon"
        elif "MA" == i_type:
            byline += "Medium Armour"
        elif "MNT" == i_type:
            byline += "Mount"
        elif "P" == i_type:
            byline += "Potion"
        elif "R" == i_type:
            byline += "Ranged Weapon"
        elif "RD" == i_type:
            byline += "Rod"
        elif "RG" == i_type:
            byline += "Ring"
        elif "RLD" == i_type:
            byline += "Reload"
        elif "S" == i_type:
            byline += "Shield"
        elif "SC" == i_type:
            byline += "Spell Scroll"
        elif "SCF" == i_type:
            byline += "Spell Focus"
        elif "SHP" == i_type:
            byline += "Ship"
        elif "T" == i_type:
            if is_property:
                byline += "Thrown"
            else:
                byline += "Tools"
        elif "TAH" == i_type:
            byline += "Transport Accessories"
        elif "TG" == i_type:
            byline += "Trade Good"
        elif "VEH" == i_type:
            byline += "Vehicle"
        elif "WD" == i_type:
            byline += "Wand"
        elif "V" == i_type:
            byline += "Versatile"
        elif "$" == i_type:
            byline += "Currency"
        elif "2H" == i_type:
            byline += "Two Handed"
        else:
            print("Unknown type : " + i_type)
            byline += i_type
        return byline + " "



