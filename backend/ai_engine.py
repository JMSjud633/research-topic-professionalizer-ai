from .models import (
    ResearchIdeaInput, ProfessionalizationResult, ScopeDiagnosis,
    FeasibilityReport, NoveltyAnalysis, TitleOption, ResearchBlueprint,
    LiteratureItem, VariableItem, RiskItem
)
from .modules.idea_analyzer import classify_domain, diagnose_scope, generate_critical_questions
from .modules.variable_extractor import extract_and_operationalize_variables
from .modules.feasibility_engine import evaluate_feasibility, detect_risks_and_biases
from .modules.title_generator import analyze_novelty, generate_title_options
from .modules.blueprint_generator import generate_blueprint
from .modules.literature_search import search_crossref_literature

def professionalize_research_idea(payload: ResearchIdeaInput, version: int = 1) -> ProfessionalizationResult:
    # 1. Classify domain & Diagnose Scope
    domain = classify_domain(payload.raw_idea, payload.target_field)
    scope = diagnose_scope(payload.raw_idea, domain)
    critical_qs = generate_critical_questions(payload.raw_idea, domain)
    
    # 2. Extract and operationalize variables
    variables = extract_and_operationalize_variables(payload.raw_idea, domain)
    
    # 3. Detect risks and biases
    risks = detect_risks_and_biases(payload.raw_idea)
    
    # 4. Feasibility engine
    feasibility = evaluate_feasibility(payload.raw_idea, payload.user_level, payload.time_constraint)
    
    # 5. Novelty analyzer
    novelty = analyze_novelty(payload.raw_idea, domain, payload.context_location)
    
    # 6. Title generation engine
    title_options = generate_title_options(payload.raw_idea, domain, payload.context_location, payload.user_level)
    
    # Pick the strongest title as default
    selected_title = title_options[1] if len(title_options) > 1 else title_options[0]
    
    # 7. Research Blueprint Generator
    blueprint = generate_blueprint(
        raw_idea=payload.raw_idea,
        domain=domain,
        selected_title_obj=selected_title,
        variables=variables,
        feasibility=feasibility,
        user_level=payload.user_level,
        location=payload.context_location
    )
    
    # 8. Literature search
    literature = search_crossref_literature(payload.raw_idea, max_results=4)
    
    return ProfessionalizationResult(
        raw_idea=payload.raw_idea,
        domain=domain,
        maturity_level=payload.user_level,
        scope_diagnosis=scope,
        critical_questions=critical_qs,
        variables=variables,
        risks_and_mitigations=risks,
        feasibility=feasibility,
        novelty=novelty,
        title_options=title_options,
        selected_title=selected_title.title,
        blueprint=blueprint,
        literature=literature,
        version=version
    )
