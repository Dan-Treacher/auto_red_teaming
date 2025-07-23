class RedTeam:
    def __init__(self, model_a, model_b):
        self.model_a = model_a
        self.model_b = model_b

    def initiate(self):
        # Starting point will be some overtly evil prompt like build me a bomb
        # This will ideally be programatically updated to tweak it until the target model actually tells you how.
        pass

    def generate_report(self):
        # Track success rates of 100 pings of the same prompt? Then after it's
        # updated to a new variant, record the prompt change and the success rates moving forward
        pass