import cProfile
import runpy
import collections
import dis
import sys
import os
import re

def generate_bytecode(file_path):
    """Generate and display bytecode for the given Python file, and write it to a file."""
    try:
        with open(file_path, 'r') as file:
            source_code = file.read()
        bytecode = compile(source_code, file_path, 'exec')
        
        # Write bytecode disassembly to a file
        output_file = f"{os.path.splitext(file_path)[0]}_bytecode.txt"
        with open(output_file, 'w') as out_file:
            dis.dis(bytecode, file=out_file)
        
        print(f"Bytecode written to {output_file}")
        return bytecode
    except Exception as e:
        print(f"Error generating bytecode: {e}")
        return None


def count_instructions(bytecode, file_path):
    """Count and display the number of instructions in the bytecode, and write it to a file."""

    instructions = []
    try:
        # Use the same function to write human-readable bytecode to a temporary file
        temp_output_file = f"{os.path.splitext(file_path)[0]}_temp_bytecode.txt"
        with open(temp_output_file, 'w') as temp_out_file:
            dis.dis(bytecode, file=temp_out_file)
        
        # Read the bytecode from the temporary file and extract instructions
        instruction_pattern = re.compile(r'\b[A-Z_]+\b')  # Regex to match all uppercase instructions
        with open(temp_output_file, 'r') as temp_in_file:
            for line in temp_in_file:
                match = instruction_pattern.search(line)
                if match:
                    instructions.append(match.group())  # Append the matched instruction
        # Clean up the temporary file
        os.remove(temp_output_file)

        print(instructions)
        instruction_counts = collections.Counter(instructions)
        output_file = f"{os.path.splitext(file_path)[0]}_instr_count.txt"
        with open(output_file, "w") as f:
            if instruction_counts:
                print("\nInstruction Counts (Highest to Lowest):")
                sorted_instruction_counts = sorted(instruction_counts.items(), key=lambda item: item[1], reverse=True)  # Sort from highest to lowest.
                for instruction, count in sorted_instruction_counts:
                    print(f"{instruction}: {count}")
                    f.write(f"{instruction}: {count}\n")

    except Exception as e:
        print(f"Error: {e}")
        return None

def run_profiler(script_to_profile):
    """Run the cProfile profiler on the specified script and save the results to a file."""
    profile_file = f"{os.path.splitext(script_to_profile)[0]}.prof"
    print(f"Profiling {script_to_profile} ...")
    
    # Use cProfile to run the target script and save stats to a file.
    cProfile.runctx("runpy.run_path(script_to_profile, run_name='__main__')", globals(), locals(), filename=profile_file)
    
    print(f"Profiling complete. Profile data saved to: {profile_file}")
    print("Run command:")
    print(f"\tsnakeviz {profile_file}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python genByteCode_v2.py <path_to_python_file>")
        return

    file_path = sys.argv[1]
    bytecode = generate_bytecode(file_path)
    if bytecode:
        count_instructions(bytecode, file_path)

    run_profiler(file_path)

if __name__ == "__main__":
    main()