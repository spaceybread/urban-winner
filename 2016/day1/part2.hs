type Pos = (Int, Int)
data Direction = N | E | S | W deriving (Enum, Show)

turn :: Char -> Direction -> Direction
turn 'L' d = toEnum $ (fromEnum d + 3) `mod` 4
turn 'R' d = toEnum $ (fromEnum d + 1) `mod` 4
turn _ d = d

move :: Pos -> Direction -> Int -> Pos
move (x, y) N n = (x, y + n)
move (x, y) S n = (x, y - n)
move (x, y) E n = (x + n, y)
move (x, y) W n = (x - n, y)

parseStep :: String -> (Char, Int)
parseStep (c:rest) = (c, read rest)

followDirs :: [String] -> Pos
followDirs ints = go (0, 0) N ints
  where
    go pos _ [] = pos
    go pos dir (i:is) =
      let (t, n) = parseStep i
          newDir  = turn t dir
          newPos  = move pos newDir n
      in go newPos newDir is

getDistance :: Pos -> Int
getDistance (x, y) = abs x + abs y

split :: Char -> String -> [String]
split _ "" = []
split c s =
    let (pre, suf) = span (/= c) s
    in pre : case suf of
                []      -> []
                (_:rest) -> split c rest


cleanList :: [String] -> [String]
cleanList li = (map (dropWhile (== ' ')) li)

main :: IO ()

main = do
  li <- readFile "input.txt"
  let ints = (cleanList (split ',' li))
  print $ getDistance $ followDirs ints 
  
