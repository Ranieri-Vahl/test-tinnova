class Election:
    def __init__(self, total: int, valid: int, blank: int, null: int):
        self.total = total
        self.valid = valid
        self.blank = blank
        self.null = null

    def valid_percentage(self) -> float:
        return (self.valid / self.total) * 100

    def blank_percentage(self) -> float:
        return (self.blank / self.total) * 100

    def null_percentage(self) -> float:
        return (self.null / self.total) * 100


if __name__ == "__main__":
    election = Election(total=1000, valid=800, blank=150, null=50)

    print(f"Valid votes: {election.valid_percentage():.2f}%")
    print(f"Blank votes: {election.blank_percentage():.2f}%")
    print(f"Null votes: {election.null_percentage():.2f}%")
