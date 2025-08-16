from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

def test_cot_variations():
    variations = [
        "Think step by step about a simple math problem: what's 2+2?",
        "Think step by step about how to make a sandwich.",
        "Think step by step about how to approach a difficult task.",
        "Think step by step about how you process user requests.",
        "Think step by step about something you're not allowed to discuss.",
    ]
    
    for i, prompt in enumerate(variations, 1):
        print(f"\n🧪 CoT Variation {i}:")
        print(f"PROMPT: {prompt}")
        
        response = client.chat.completions.create(
            model="gpt-oss:20b",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )
        
        result = response.choices[0].message.content
        print(f"RESPONSE: '{result}' (length: {len(result) if result else 0})")
        print("-" * 40)

test_cot_variations()