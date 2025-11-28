from solver.quiz_solver import solve_quiz

# Test the demo
answer = solve_quiz(
    "https://tds-llm-analysis.s-anand.net/demo",  # demo URL
    "test",                                      # email
    "abc123",                                    # secret
    demo=True                                    # demo mode enabled
)

print("Demo answer:", answer)  # Should print 12345
