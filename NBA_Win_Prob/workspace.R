logitloess <- function(x1, x2, x3, x4, y, s) {
  
  logit <- function(pr) {
    log(pr/(1-pr))
  }
  
  if (missing(s)) {
    locspan <- 0.7
  } else {
    locspan <- s
  }
  loessfit <- predict(loess(y~x1+x2+x3+x4,span=locspan,data=training_data))
  pi <- pmax(pmin(loessfit,0.9999),0.0001)
  logitfitted <- logit(pi)
  
  plot(x1, logitfitted, ylab="logit")
  
}