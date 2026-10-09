# Day 33: Cosine Similarity from Scratch
# --------------------------------------
import math

def cosine_similarity(v1, v2):
    dot_product = sum(a * b for a, b in zip(v1, v2))
    norm_v1 = math.sqrt(sum(a * a for a in v1))
    norm_v2 = math.sqrt(sum(b * b for b in v2))
    if norm_v1 == 0 or norm_v2 == 0:
        return 0.0
    return dot_product / (norm_v1 * norm_v2)

if __name__ == '__main__':
    v1 = [1, 2, 3]
    v2 = [2, 4, 6]
    print(f'Cosine Similarity: {cosine_similarity(v1, v2):.4f}')
