import random
from core.sigma import sigma

def run_system(lambda_val, delta=0.1, steps=50):
    x = [random.random() for _ in range(10)]
    transitions = 0

    for t in range(steps):
        noise = [xi + lambda_val * random.gauss(0, 1) for xi in x]

        s1 = sigma(x)
        s2 = sigma(noise)

        if abs(s2 - s1) > delta:
            transitions += 1

        x = noise

    return transitions

def main():
    for lam in [0.1, 0.5, 0.9]:
        t = run_system(lam)

        print(f"[λ={lam}]")
        print("Transitions:", t)
        print("-" * 30)

if __name__ == "__main__":
    main()