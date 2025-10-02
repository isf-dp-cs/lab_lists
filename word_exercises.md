# Word Exercises

Answer the following questions (or at least as many as you can figure out) in this document. 


## 1. What is the longest word?

How did you figure it out? 

```python
for i in range(0,30):
    print(i,len(get_words_of_length(words, i)))

print(get_words_of_length(words, 18))
```

What is the answer?
```shell

```

## 2. Which words contain the word "ability"? 

How did you figure it out? 

```python
for word in get_words_including(words, 'ability'):
    print(word)

print(get_words_of_length(words, 18))
```

What is the answer?
```shell
ability
accountability
availability
capability
disability
inability
liability
probability
reliability
stability
```

## 3. How many words have the word "cat" in them?

How did you figure it out? 

```python
print(len(get_words_including(words, 'cat')))
```

What is the answer?
```shell
67
```

## 4. Which words contain double 'o's and double 's's. 

How did you figure it out? 

```python
for word in get_words_including(get_words_including(words, 'oo'),'ss'):
    print(word)
```

What is the answer?
```shell
classroom
goodness
```


## 5. Which words have all five vowels (aeiou)?

How did you figure it out? 

```python
vowel_words = get_words_including(get_words_including(get_words_including(get_words_including(get_words_including(words, 'a'),'e'),'i'),'o'),'u')
for word in vowel_words:
    print(word)
```

What is the answer?
```shell
authorities
authorized
automobile
automotive
behaviour
boundaries
communicate
dialogue
documentation
education
educational
encouraging
equation
equations
evaluation
evolutionary
favourite
questionable
regulation
regulations
reputation
revolutionary
simultaneously
speculation
telecommunications
```