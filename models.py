from dataclasses import dataclass
from enum import Enum
from typing import List

@dataclass
class QuestionSection:
    code: str
    name: str
    categoryCode: str
    categoryName: str
    sort: int
    isSubjective: bool
    '''是否为客观题'''
    score: int

@dataclass 
class QuestionDifficulty:
    code: str
    name: str
    value: int

@dataclass
class QuestionKnowledges:
    code: str
    name: str
    weight: float
    '''权重'''

@dataclass
class Question:
    id: str
    number: str
    section: QuestionSection
    materials: list
    difficulty: QuestionDifficulty
    knowledges: List[QuestionKnowledges]
    commonKnowledges: List[QuestionKnowledges]
    usedPapers: List[str]
    contentHtml: str
    '''手动解析originalStruct.contentHtml'''
    score: float
    paperName: str
    '''何处来的题目'''
    answerImg: str
    analysisImg: str
    createTime: str
    '''题目创建时间'''
    isXGKQuestion: bool
    '''是否为新高考'''

@dataclass
class Knowledge:
    id: str
    name: str
    isChild: bool
    '''是否为子知识'''
    parentKnowledgeId: str
    '''如果是，上一级的知识ID'''

@dataclass
class TextBookChapter:
    chapterId: str = None
    '''教科书章节的编号'''
    chapterName: str = None
    '''章节名'''
    chapterType: str = None 
    '''本章节的类型，有unit和course'''