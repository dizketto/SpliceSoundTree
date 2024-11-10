from _typeshed import Incomplete

from antlr4 import DFA as DFA
from antlr4.atn.ATN import ATN as ATN
from antlr4.atn.ATNConfig import ATNConfig as ATNConfig
from antlr4.atn.ATNConfigSet import ATNConfigSet as ATNConfigSet
from antlr4.atn.ATNSimulator import ATNSimulator as ATNSimulator
from antlr4.atn.ATNState import ATNState as ATNState, DecisionState as DecisionState, RuleStopState as RuleStopState
from antlr4.atn.PredictionMode import PredictionMode as PredictionMode
from antlr4.atn.SemanticContext import SemanticContext as SemanticContext, andContext as andContext, orContext as orContext
from antlr4.atn.Transition import (
    ActionTransition as ActionTransition,
    AtomTransition as AtomTransition,
    NotSetTransition as NotSetTransition,
    PrecedencePredicateTransition as PrecedencePredicateTransition,
    PredicateTransition as PredicateTransition,
    RuleTransition as RuleTransition,
    SetTransition as SetTransition,
    Transition as Transition,
)
from antlr4.BufferedTokenStream import TokenStream as TokenStream
from antlr4.dfa.DFAState import DFAState as DFAState, PredPrediction as PredPrediction
from antlr4.error.Errors import NoViableAltException as NoViableAltException
from antlr4.Parser import Parser as Parser
from antlr4.ParserRuleContext import ParserRuleContext as ParserRuleContext
from antlr4.PredictionContext import (
    PredictionContext as PredictionContext,
    PredictionContextCache as PredictionContextCache,
    PredictionContextFromRuleContext as PredictionContextFromRuleContext,
    SingletonPredictionContext as SingletonPredictionContext,
)
from antlr4.RuleContext import RuleContext as RuleContext
from antlr4.Token import Token as Token
from antlr4.Utils import str_list as str_list

class ParserATNSimulator(ATNSimulator):
    debug: bool
    trace_atn_sim: bool
    dfa_debug: bool
    retry_debug: bool
    parser: Incomplete
    decisionToDFA: Incomplete
    predictionMode: Incomplete
    mergeCache: Incomplete
    def __init__(
        self, parser: Parser, atn: ATN, decisionToDFA: list[DFA], sharedContextCache: PredictionContextCache
    ) -> None: ...
    def reset(self) -> None: ...
    def adaptivePredict(self, input: TokenStream, decision: int, outerContext: ParserRuleContext): ...
    def execATN(self, dfa: DFA, s0: DFAState, input: TokenStream, startIndex: int, outerContext: ParserRuleContext): ...
    def getExistingTargetState(self, previousD: DFAState, t: int): ...
    def computeTargetState(self, dfa: DFA, previousD: DFAState, t: int): ...
    def predicateDFAState(self, dfaState: DFAState, decisionState: DecisionState): ...
    def execATNWithFullContext(
        self, dfa: DFA, D: DFAState, s0: ATNConfigSet, input: TokenStream, startIndex: int, outerContext: ParserRuleContext
    ): ...
    def computeReachSet(self, closure: ATNConfigSet, t: int, fullCtx: bool): ...
    def removeAllConfigsNotInRuleStopState(self, configs: ATNConfigSet, lookToEndOfRule: bool): ...
    def computeStartState(self, p: ATNState, ctx: RuleContext, fullCtx: bool): ...
    def applyPrecedenceFilter(self, configs: ATNConfigSet): ...
    def getReachableTarget(self, trans: Transition, ttype: int): ...
    def getPredsForAmbigAlts(self, ambigAlts: set[int], configs: ATNConfigSet, nalts: int): ...
    def getPredicatePredictions(self, ambigAlts: set[int], altToPred: list[int]): ...
    def getSynValidOrSemInvalidAltThatFinishedDecisionEntryRule(self, configs: ATNConfigSet, outerContext: ParserRuleContext): ...
    def getAltThatFinishedDecisionEntryRule(self, configs: ATNConfigSet): ...
    def splitAccordingToSemanticValidity(self, configs: ATNConfigSet, outerContext: ParserRuleContext): ...
    def evalSemanticContext(self, predPredictions: list[Incomplete], outerContext: ParserRuleContext, complete: bool): ...
    def closure(
        self,
        config: ATNConfig,
        configs: ATNConfigSet,
        closureBusy: set[Incomplete],
        collectPredicates: bool,
        fullCtx: bool,
        treatEofAsEpsilon: bool,
    ): ...
    def closureCheckingStopState(
        self,
        config: ATNConfig,
        configs: ATNConfigSet,
        closureBusy: set[Incomplete],
        collectPredicates: bool,
        fullCtx: bool,
        depth: int,
        treatEofAsEpsilon: bool,
    ): ...
    def closure_(
        self,
        config: ATNConfig,
        configs: ATNConfigSet,
        closureBusy: set[Incomplete],
        collectPredicates: bool,
        fullCtx: bool,
        depth: int,
        treatEofAsEpsilon: bool,
    ): ...
    def canDropLoopEntryEdgeInLeftRecursiveRule(self, config): ...
    def getRuleName(self, index: int): ...
    epsilonTargetMethods: Incomplete
    def getEpsilonTarget(
        self, config: ATNConfig, t: Transition, collectPredicates: bool, inContext: bool, fullCtx: bool, treatEofAsEpsilon: bool
    ): ...
    def actionTransition(self, config: ATNConfig, t: ActionTransition): ...
    def precedenceTransition(
        self, config: ATNConfig, pt: PrecedencePredicateTransition, collectPredicates: bool, inContext: bool, fullCtx: bool
    ): ...
    def predTransition(
        self, config: ATNConfig, pt: PredicateTransition, collectPredicates: bool, inContext: bool, fullCtx: bool
    ): ...
    def ruleTransition(self, config: ATNConfig, t: RuleTransition): ...
    def getConflictingAlts(self, configs: ATNConfigSet): ...
    def getConflictingAltsOrUniqueAlt(self, configs: ATNConfigSet): ...
    def getTokenName(self, t: int): ...
    def getLookaheadName(self, input: TokenStream): ...
    def dumpDeadEndConfigs(self, nvae: NoViableAltException): ...
    def noViableAlt(self, input: TokenStream, outerContext: ParserRuleContext, configs: ATNConfigSet, startIndex: int): ...
    def getUniqueAlt(self, configs: ATNConfigSet): ...
    def addDFAEdge(self, dfa: DFA, from_: DFAState, t: int, to: DFAState): ...
    def addDFAState(self, dfa: DFA, D: DFAState): ...
    def reportAttemptingFullContext(
        self, dfa: DFA, conflictingAlts: set[Incomplete], configs: ATNConfigSet, startIndex: int, stopIndex: int
    ): ...
    def reportContextSensitivity(self, dfa: DFA, prediction: int, configs: ATNConfigSet, startIndex: int, stopIndex: int): ...
    def reportAmbiguity(
        self,
        dfa: DFA,
        D: DFAState,
        startIndex: int,
        stopIndex: int,
        exact: bool,
        ambigAlts: set[Incomplete],
        configs: ATNConfigSet,
    ): ...
