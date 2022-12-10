use std::fs::File;
use std::io::{self, prelude::*, BufReader};

fn main() -> io::Result<()> {
    let reader = BufReader::new(File::open("input.txt")?);
    let mut timeline: Vec<(i32, i32)> = Vec::new();
    let mut counter = 0;
    let mut x = 1;
    let mut quant = 20;
    let mut result = 0;
    timeline.push((counter, x));
    for line in reader.lines() {
      let line_s = line.unwrap();
      let mut split = line_s.split_whitespace();
      let cmd = split.next().unwrap();
      let diff :i32;
      let time;
      if cmd == "addx" {
        diff = split.next().unwrap().parse().unwrap(); 
        time = 2;
      } else {
        diff = 0;
        time = 1;
      }
      counter += time;
      if counter >= quant {
          result += quant * x;
          println!("@{}: {}", quant, x);
          quant += 40;
      }
      x += diff;
      if diff != 0 {
        timeline.push((counter, x))
      }
    }
    dbg!(result);

    Ok(())
}
