# Script for displaying results of ES latency
# Please refer to queries.py for the list of queries
search_results <- read.delim("~/search_results.csv", header=FALSE)
df2 = data.frame(search_results)
df2[] <- lapply(search_results, as.character)
df2[] <- lapply(df2, function(y) as.character(gsub(",", "",y)))
df2$V4 = as.numeric(df2$V4)
df2$V2 = as.factor(df2$V2)
df2$V2 = ifelse(df2$V2 == "match", "m", 
                ifelse(df2$V2 == "match_phrasesimple", "mp_sim", 
                       ifelse(df2$V2 == "match_phrasestandard", "mp_std",  
                              ifelse(df2$V2 == "match_phrasestop", "mp_stp", 
                                     ifelse(df2$V2 == "more like this", "mlt", 
                                            ifelse(df2$V2 == "more like thisstop", "mlt", 
                                                   ifelse(df2$V2 == "match + fuzzy", "m_f", "m_f")))))))

dfAA = df2[df2$V3 == "Attribute Error",]
dfLL = df2[df2$V3 != "Attribute Error",]

boxplot(dfAA$V4~dfAA$V2,
        main="Latency vs. Query Type", 
        ylab="Latency, sec")
boxplot(dfLL$V4~dfLL$V2,
        main="Latency vs. Query Type", 
        ylab="Latency, sec")

dfMP = dfLL[dfLL$V2 %in% c("mp_sim", "mp_std", "mp_stp"),]

boxplot(dfMP$V4~dfMP$V2,
        main="Latency vs. Query Type", 
        ylab="Latency, sec")

# The difference between these two files is that the ingestion was
# larger for the queries.py file; please refer to RuntimeErrors.py 
# The input was the attribute object.long_st
match_phrase_long <- read.delim("~/debugDemyst/match_phrase_long.csv", header=FALSE)
dfmfl = data.frame(match_phrase_long)
boxplot(dfmfl$V3~dfmfl$V2,
        main="Latency vs. Query Type", 
        ylab="Latency, sec")