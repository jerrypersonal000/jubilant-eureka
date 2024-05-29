import streamlit as st
from collections import deque

def shortest_path_to_range(A, B, C):
    queue = deque([(A, 0, [])])
    visited = set()
    operations = list(range(1, 10))
    max_limit = 30000  # Adjusted limit to 30000

    while queue:
        current, steps, path = queue.popleft()
        
        if B <= current <= C:
            return steps, path
        
        if abs(current) > max_limit:
            continue
        
        for op in operations:
            next_steps = [
                (current + op, f"{current} + {op} = {current + op}"),
                (current - op, f"{current} - {op} = {current - op}"),
                (current * op, f"{current} * {op} = {current * op}"),
                (current // op if op != 0 else None, f"{current} // {op} = {current // op}" if op != 0 else None)
            ]
            for result, desc in next_steps:
                if result is not None and result not in visited and abs(result) <= max_limit:
                    visited.add(result)
                    queue.append((result, steps + 1, path + [desc]))
    
    return -1, []

# Initialize session state variables if not already initialized
if 'A' not in st.session_state:
    st.session_state.A = ""
if 'B' not in st.session_state:
    st.session_state.B = ""
if 'C' not in st.session_state:
    st.session_state.C = ""

# Input fields
st.session_state.A = st.text_input("Enter the initial value A: ", value=st.session_state.A)
st.session_state.B = st.text_input("Enter the lower bound B: ", value=st.session_state.B)
st.session_state.C = st.text_input("Enter the upper bound C: ", value=st.session_state.C)

# Clear button
if st.button("Clear"):
    st.session_state.A = ""
    st.session_state.B = ""
    st.session_state.C = ""
    st.experimental_rerun()

# Convert inputs to integers
try:
    A = int(st.session_state.A)
    B = int(st.session_state.B)
    C = int(st.session_state.C)

    steps, path = shortest_path_to_range(A, B, C)
    if steps != -1:
        st.write(f"The shortest path from {A} to the range [{B}, {C}] takes {steps} steps")
        st.write("The steps are as follows:")
        for p in path:
            st.write(p)
    else:
        st.write(f"No path found from {A} to the range [{B}, {C}].")
except ValueError:
    st.write("Please enter valid integer values for A, B, and C.")
