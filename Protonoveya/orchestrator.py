# orchestrator.py — Central module to coordinate agent logic and semantic modules

from sigma_avatarus import SigmaAvatarus
from fdl_agent_kernel.logic_core import FDLKernel
from fdl_codeagents.api_wrapper import FDLCodeAgent
from modules.gromada_sdk.constitution_core import GromadaConstitution
from modules.Δψ_monitor.lie_tension_analyzer import analyze_tension

def initialize_agent():
    avatar = SigmaAvatarus()
    kernel = FDLKernel()
    agent = FDLCodeAgent(api_key="your-openai-key", kernel=kernel)
    constitution = GromadaConstitution()
    constitution.load_guardians_from_file()
    return avatar, kernel, agent, constitution

def scenario_execution(phrase):
    avatar, kernel, agent, _ = initialize_agent()
    resonance = avatar.resonate(phrase)
    synthesis = kernel.analyze(phrase, resonance)
    tension = analyze_tension(phrase)
    response = agent.query(phrase, resonance)

    return {
        "input": phrase,
        "resonance": resonance,
        "synthesis": synthesis,
        "tension": tension,
        "response": response
    }

if __name__ == "__main__":
    sample = scenario_execution("Гармония возможна только через честность.")
    for k, v in sample.items():
        print(f"{k.upper()}: {v}")
