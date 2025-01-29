from deepeval.synthesizer import Synthesizer
from deepeval.synthesizer.config import ContextConstructionConfig
from deepeval.synthesizer.config import EvolutionConfig
from deepeval.synthesizer import Evolution
from dotenv import load_dotenv

load_dotenv()

def generateGoldens():
    synthesizer = Synthesizer(
        evolution_config=EvolutionConfig(evolutions={
            Evolution.REASONING: 1/7,
            Evolution.MULTICONTEXT: 1/7,
            Evolution.CONCRETIZING: 1/7,
            Evolution.CONSTRAINED: 1/7,
            Evolution.COMPARATIVE: 1/7,
            Evolution.HYPOTHETICAL: 1/7,
            Evolution.IN_BREADTH: 1/7,
        },
        num_evolutions=1)
    )
    synthesizer.generate_goldens_from_docs(
        document_paths=['../document-base/sf-csv.txt',
                        '../document-base/sf-report.pdf',
                        '../document-base/rag-tech-stack.txt',
                        '../document-base/permissions-tutorial-2.txt',
                        '../document-base/permissions-tutorial-2-5.txt',
                        '../document-base/paragon-slack-questions.txt'],
        context_construction_config=ContextConstructionConfig(chunk_size=200, chunk_overlap=20),
    )
    
    golden_dataframe = synthesizer.to_pandas()
    golden_dataframe.to_csv('../document-base/golden.csv')

generateGoldens()
