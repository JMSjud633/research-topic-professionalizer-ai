from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

class ResearchIdeaInput(BaseModel):
    raw_idea: str
    user_level: Optional[str] = "Level 3 — Advanced (Undergraduate / Sarjana)"
    target_field: Optional[str] = "Auto-detect"
    context_location: Optional[str] = ""
    available_data: Optional[str] = ""
    time_constraint: Optional[str] = "3-6 months"
    intended_method: Optional[str] = "Auto-recommend"
    api_key: Optional[str] = None
    provider: Optional[str] = "internal" # "internal", "gemini", "openai"

class ScopeDiagnosis(BaseModel):
    status: str # "Too broad", "Appropriate", "Too narrow"
    explanation: str
    recommended_focus: str

class VariableItem(BaseModel):
    variable: str
    category: str # "Independent Variable", "Dependent Variable", "Control Variable", "Confounding Variable"
    definition: str
    indicator: str
    measurement: str
    instrument: str

class FeasibilityScoreDetail(BaseModel):
    dimension: str
    score: int # 0 to 5
    rating: str # "Reasonable", "Good", etc.
    analysis: str
    recommendation: str

class FeasibilityReport(BaseModel):
    total_score: float # out of 5
    percentage: float
    status: str
    details: List[FeasibilityScoreDetail]

class RiskItem(BaseModel):
    risk_type: str # "Confirmation Bias", "Confounding Variables", etc.
    explanation: str
    solution: str

class NoveltyAnalysis(BaseModel):
    topic_novelty: str
    methodological_novelty: str
    contextual_novelty: str
    practical_novelty: str
    potential_novelty_statement: str

class TitleOption(BaseModel):
    category: str # "Option A — Conservative Academic", etc.
    title: str
    strength: str
    weakness: str
    suitable_method: str
    difficulty_level: str
    recommended_researcher_level: str
    scores: Dict[str, float] # clarity, specificity, researchability, feasibility, academic_quality, objectivity, potential_novelty
    overall_score: float

class ResearchBlueprint(BaseModel):
    proposed_title: str
    research_field: str
    research_problem: str
    research_background: str
    research_gap: str
    research_objective: str
    research_questions: List[str]
    hypotheses: Optional[List[str]] = None
    independent_variables: List[str]
    dependent_variables: List[str]
    control_variables: List[str]
    confounding_variables: List[str]
    research_design: str
    population: str
    sample: str
    sampling_technique: str
    data_collection: str
    research_instruments: str
    data_analysis: str
    recommended_statistical_methods: List[str]
    expected_contribution: str
    potential_limitations: str
    ethical_considerations: str
    feasibility_score: str
    research_maturity_level: str

class LiteratureItem(BaseModel):
    title: str
    authors: List[str]
    year: Optional[str] = None
    doi: Optional[str] = None
    url: Optional[str] = None
    journal: Optional[str] = None
    relevance: str

class ProfessionalizationResult(BaseModel):
    raw_idea: str
    domain: str
    maturity_level: str
    scope_diagnosis: ScopeDiagnosis
    critical_questions: List[str]
    variables: List[VariableItem]
    risks_and_mitigations: List[RiskItem]
    feasibility: FeasibilityReport
    novelty: NoveltyAnalysis
    title_options: List[TitleOption]
    selected_title: str
    blueprint: ResearchBlueprint
    literature: List[LiteratureItem]
    version: int = 1
