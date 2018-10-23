# This script generates plots for my insight project: Debugging Demystified.
# The script plots latency and evaluates accuracy.  Please see the following 
# supporting python files that generated the output: 
# 1. match.py                   writes: accuracy_match.csv
# 2. match_phrase.py            writes: accuracy_filter.csv
#                               writes: accuracy.csv
# 3. more_like_this_query.py    writes: accuracy_more_like_this.csv
# 4. RuntimeErrors.py

library(dplyr)
library(plyr)
library(stringr)
library(ggplot2)

drive = paste(getwd(), "latency/data/", sep="/")
match = "accuracy_match.csv"
match_phrase_filter = "accuracy_filter.csv"
match_phrase = "accuracy.csv"
more_like_this = "accuracy_more_like_this.csv"

cleanup  = function(path, file){
  import_csv = read.delim(paste(path, file, sep=""), header=FALSE)
  import_csv$V1 = as.character(gsub(",", "", import_csv$V1))        # removes  ","
  import_csv$V4 = as.character(gsub(",", "", import_csv$V4))        # removes, ","
  if ("V5" %in% colnames(import_csv)) {
    import_csv$V5 = as.character(gsub(",", "", import_csv$V5))      # removes, ","
    import_csv$V5 = as.numeric(import_csv$V5)
  }
  df = data.frame(import_csv)
  t.df = df %>% 
    tidyr::separate("V1", c("V1", "V15"), ":")    # creates two columns on ";" split
  t.df$V1 = as.factor(t.df$V1)                    
  t.df$V2 = as.factor(t.df$V2)
  t.df$V4 = as.numeric(t.df$V4)
  return(t.df)
}

# V1  = "Error"
# V15 = "Error Description"
# V2  = "Query function"
# V3  = "Latency"
# V5  = "Slop" How many words in between can exists 

acc_match = cleanup(drive, match)
acc_mf_f  = cleanup(drive, match_phrase_filter)
acc_mf    = cleanup(drive, match_phrase)
acc_mlt   = cleanup(drive, more_like_this)

# plots match results
ggplot(data = acc_match) + 
  geom_boxplot(aes(x=V1, y=V3)) + 
  facet_grid(~V2) + 
  labs(y="Latency, sec", x="Stack Trace") + 
  ggtitle("Match")
  
# plots match_phrase results: filter
ggplot(data = acc_mf_f) +
  geom_boxplot(aes(x=V2, y=V3)) + 
  facet_grid(~V1~V4) + 
  labs(y="Latency, sec", x="Analyzer") + 
  ggtitle("Match Phrase: filters questions")

# group attributes, slop and accuracy for match_phrase filter
acc_mf_f_agg = acc_mf_f %>%
                group_by(V1, V4, V2) %>% 
                dplyr::summarize(median=median(V3), acc = sum(V5)/n())

# plots match_phrase results: no filter
ggplot(data = acc_mf) + 
  geom_boxplot(aes(x=V2, y=V3)) + 
  facet_grid(~V1~V4) + 
  labs(y="Latency, sec", x="Analyzer") +  
  ylim(0, 0.05) + 
  ggtitle("Match Phrase")

# group attributes, slop and accuracy for match_phrase filter
acc_mf_agg = acc_mf %>%
  group_by(V1, V4, V2) %>% 
  dplyr::summarize(median=median(V3), acc = sum(V5)/n())

# More like this
ggplot(data = acc_mlt) + 
  geom_boxplot(aes(x=V1, y=V3)) + 
  ggtitle("More Like This") + 
  labs(y="Latency, sec", x="Analyzer")