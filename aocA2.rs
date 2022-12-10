use std::fs::File;
use std::io::{self, prelude::*, BufReader};

fn main() -> io::Result<()> {
    let reader = BufReader::new(File::open("input.txt")?);
    let mut lines = reader.lines();
    let mut x : i32 = 1;
    let mut wait = 1;
    let mut diff = 0;
    for ray in 1..240 {
        wait -= 1;
        if wait == 0 {
          x += diff;
          let line = lines.next().unwrap().unwrap();
          let mut split = line.split_whitespace();
          let cmd = split.next().unwrap();
          if cmd == "addx" {
             diff = split.next().unwrap().parse().unwrap(); 
             wait = 2;
           } else {
              diff = 0;
              wait = 1;
           }
        }
        let col = (ray - 1) % 40;
        let c = if (x - col).abs() <= 1 { '#' } else { '.' };
        print!("{}", c);
        if col == 39 {
          print!("\n");
        }
    }

    Ok(())
}
