from random import choice, shuffle
from re import sub, search

from bulme_utils import reflect, tidy_up, remove_punctuations


class Eliza:

    def __init__(self, script):
        self.script = script
        self.given_answers = set()


    def welcome(self):
        return choice(self.script.WELCOME_PHRASES)


    def goodbye(self):
        return choice(self.script.GOODBYE_PHRASES)


    @staticmethod
    def _create_candidate(match_obj, answer_pattern):
        text = match_obj.string
        text = remove_punctuations(text)
        
        # extract values for placeholders
        complete = reflect(text)
        pre_match = text[:match_obj.start()-1]
        pre_match = reflect(pre_match)
        match = text[match_obj.start():match_obj.end()]
        post_match = text[match_obj.end()+1:]
        post_match = reflect(post_match)
        
        # substitute placeholders
        candidate = answer_pattern
        candidate = sub("%COMPLETE", complete, candidate)
        candidate = sub("%PRE_MATCH", pre_match, candidate)
        candidate = sub("%MATCH", match, candidate)
        candidate = sub("%POST_MATCH", post_match, candidate)

        return candidate


    def answer(self, text):
        text = tidy_up(text)

        for rule in self.script.rules:
            search_pattern = rule[0]
            answer_patterns = rule[1]

            match_obj = search(search_pattern, text)

            if match_obj:
                shuffle(answer_patterns)
                
                for answer_pattern in answer_patterns:
                    candidate = self._create_candidate(match_obj, answer_pattern)
                    if candidate not in self.given_answers:
                        answer = candidate
                        self.given_answers.add(answer)
                        return answer
                    else:
                        continue

        return choice(self.script.DEFAULT_ANSWERS)
