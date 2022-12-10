use std::fs::File;
use std::io::{self, prelude::*, BufReader};

fn main() -> io::Result<()> {
    let reader = BufReader::new(File::open("input.txt")?);
    let mut timeline: Vec<(i32, i32)> = Vec::new();
    let mut counter = 1;
    let mut x = 1;
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
      x += diff;
      if diff != 0 {
        timeline.push((counter, x))
      }
    }
    let mut tmidx = 0;
    for ray in 1..240 {
        let col = (ray - 1) % 40 + 1;
        let c = if (timeline[tmidx].1 - col).abs() <= 1 { '#' } else { '.' };
        print!("{}", c);
        if timeline[tmidx].0 < ray {
            tmidx += 1
        }
        if col == 40 {
          print!("\n");
        }
    }

    Ok(())
}
